First have a look at the RequirementsForFactories and the TermsOfUse, and maybe sign up with the [mailing list](http://lists.browsershots.org/mailman/listinfo/browsershots-factories).

I have recently implemented the web-based user registration for Browsershots. You can register a new user account and then create screenshot factories. Start here: https://browsershots.org/accounts/email/

Please [let me know](mailto:johann@browsershots.org) if you find problems or have any ideas for improvement, especially how to make it more intuitive and user-friendly.

## Find your computer's name ##

The name for your screenshot factory will be your computer's name by default. Here's how you find it:

  * On Windows: click Start, click Control Panel, click System, and then click the Computer Name tab.
  * On Unix (Linux and Mac OS X): run the **hostname** command.

But you can also choose a different name for your ShotFactory and then run it with **shotfactory -f yourname**.

## Install the software ##

We have installation instructions for the following platforms:

  * InstallFactoryLinux
  * InstallFactoryWindows
  * InstallFactoryMac

## Add your browsers ##

After your screenshot factory is created, you can add browsers to it. In Browsershots 0.4, there's a simple web interface for that. It is no longer necessary to email the User-Agent strings to me.

  * Visit the page http://browsershots.org/browsers/add/ with each of your installed browsers.
  * Check that the auto-detected browser settings are correct, or adjust them manually.
  * Send a screenshot to [johann@browsershots.org](mailto:johann@browsershots.org) if you find errors.
  * Select your screenshot factory name from the drop-down list, enter your password, click submit.
  * If you want to change the settings for a browser, just submit it again. Your old entry will be updated or replaced automatically.