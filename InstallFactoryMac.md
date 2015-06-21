## Install prerequisites ##

  * [Subversion Binaries](http://www.codingmonkeys.de/mbo/)
> > (or **sudo port install subversion**)
  * [NetPBM tools](http://netpbm.sourceforge.net/)
> > (or **sudo port install netpbm**, or

> [binaries from Gallery](http://sourceforge.net/project/showfiles.php?group_id=7130&package_id=14464))
  * [Python appscript module](http://appscript.sourceforge.net/py-appscript/install.html)
> > (or **sudo easy\_install appscript**)
  * [cscreen](http://www.versiontracker.com/dyn/moreinfo/macosx/19753)
> > to change screen resolution
> > ([mirror](http://download.browsershots.org/thirdparty/cscreen.dmg))

And if you want to support more media formats:

  * Windows Media Player

> [for Mac OS X](http://www.apple.com/downloads/macosx/video/windowsmediaplayerformacosx.html)
> ([alternate link, also for Mac OS 8.1-9](http://www.microsoft.com/mac/otherproducts/otherproducts.aspx?pid=windowsmedia))

## Get the source code ##

Check out the source code from the Subversion repository:

```
svn checkout http://svn.browsershots.org/trunk/shotfactory
```

Also copy the cscreen program into the **shotfactory** directory.

Starting with milestone:0.3-beta1, global installation with **python setup.py install** is no longer required.

## Settings ##

  * Disable the screensaver.
  * Set the desktop background to white.
  * For each browser that you want to run:
    * Set it to start with an empty page.
    * Hide the bookmark bar.
    * Show the status bar.

If you want to run browsers other than Safari, also follow these steps:

  * System Preferences
  * Universal Access
  * Enable access for assistive devices

## Run ##

```
cd shotfactory
python shotfactory.py
```

See InstallFactory for registration and troubleshooting tips.

## Fast User Switching ##

On Mac OS X 10.4 and 10.5, you can run the screenshot factory in the background if you enable Fast User Switching. Also, your personal files and browser history etc. are safe if you use a separate user account. To enable Fast User Switching, follow these steps:

  * System Preferences
  * Accounts
  * Login Options
  * Enable fast user switching

Then you can create a separate user (e.g. `shotfactory1`) for the screenshot factory. This user does not need admin privileges. Switch to this user account before you start the screenshot factory.