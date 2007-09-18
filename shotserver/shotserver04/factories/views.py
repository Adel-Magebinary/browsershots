# browsershots.org - Test your web design in different browsers
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
#
# Browsershots is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Browsershots is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Factory views.
"""

__revision__ = "$Rev$"
__date__ = "$Date$"
__author__ = "$Author$"

from psycopg import IntegrityError
from django.http import Http404, HttpResponseRedirect
from django.utils.text import capfirst
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import newforms as forms
from django.newforms.util import ErrorList
from shotserver04 import settings
from shotserver04.common import last_poll_timeout, error_page
from shotserver04.factories.models import Factory
from shotserver04.browsers.models import Browser
from shotserver04.screenshots.models import Screenshot, ProblemReport
from shotserver04.common.preload import preload_foreign_keys


def overview(http_request):
    """
    List all screenshot factories.
    """
    factory_table_header = Factory.table_header()
    factory_list = Factory.objects.select_related().filter(
        last_poll__gt=last_poll_timeout()).order_by('-uploads_per_day')
    if not len(factory_list):
        return error_page(http_request, _("out of service"),
            _("No active screenshot factories."),
            _("Please try again later."))
    return render_to_response('factories/overview.html', locals(),
        context_instance=RequestContext(http_request))


def details(http_request, name):
    """
    Get detailed information about a screenshot factory.
    """
    try:
        factory = Factory.objects.get(name=name)
    except Factory.DoesNotExist:
        raise Http404
    browser_list = list(Browser.objects.filter(factory=factory.id))
    preload_foreign_keys(browser_list,
                         browser_group=True,
                         engine=True,
                         javascript=True,
                         java=True,
                         flash=True)
    browser_list.sort(key=lambda browser: (unicode(browser), browser.id))
    screensize_list = factory.screensize_set.all()
    colordepth_list = factory.colordepth_set.all()
    screenshot_list = Screenshot.objects.filter(factory=factory,
        website__profanities__lte=settings.PROFANITIES_ALLOWED)
    screenshot_list = screenshot_list.order_by('-id')[:10]
    preload_foreign_keys(screenshot_list, browser=browser_list)
    admin_logged_in = http_request.user.id == factory.admin_id
    show_commands = admin_logged_in and True in [
        bool(browser.command) for browser in browser_list]
    problems_list = ProblemReport.objects.filter(
        screenshot__factory=factory)[:10]
    return render_to_response('factories/details.html', locals(),
        context_instance=RequestContext(http_request))


class FactoryBase(forms.BaseForm):
    def clean_name(self):
        """
        Check that the factory name is sensible.
        """
        NAME_CHAR_FIRST = 'abcdefghijklmnopqrstuvwxyz'
        NAME_CHAR = NAME_CHAR_FIRST + '0123456789_-'
        name = self.cleaned_data['name']
        if name[0] not in NAME_CHAR_FIRST:
            raise forms.ValidationError(unicode(
                _("Name must start with a lowercase letter.")))
        for index in range(len(name)):
            if name[index] not in NAME_CHAR:
                raise forms.ValidationError(unicode(
_("Name may contain only lowercase letters, digits, underscore, hyphen.")))
        if name in 'localhost server factory shotfactory add'.split():
            raise forms.ValidationError(unicode(
                _("This name is reserved.")))
        return name

    def create_factory(self, admin):
        """
        Try to create the factory in the database.
        Return None if the factory name is already taken.
        """
        factory = self.save(commit=False)
        factory.admin = admin
        try:
            factory.save()
            return factory
        except IntegrityError, e:
            transaction.rollback()
            if 'duplicate' in str(e).lower():
                self.errors['name'] = ErrorList([
                    _("This name is already taken.")])
            else:
                self.errors[forms.NON_FIELD_ERRORS] = ErrorList([str(e)])


FactoryForm = forms.form_for_model(Factory, form=FactoryBase,
    fields=('name', 'architecture', 'operating_system'))


@login_required
def add(http_request):
    factory = None
    form = FactoryForm(http_request.POST or None)
    if form.is_valid():
        factory = form.create_factory(http_request.user)
    if not factory:
        form_title = _("register a new screenshot factory")
        form_submit = _("register")
        form_javascript = "document.getElementById('id_name').focus()"
        return render_to_response('form.html', locals(),
            context_instance=RequestContext(http_request))
    return HttpResponseRedirect(factory.get_absolute_url())