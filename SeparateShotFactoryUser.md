It is highly recommended to run the screenshot factory script on a separate user account, for the following reasons:

  * Your personal files are safe from privacy exploits.
  * Your personal browsing history and bookmarks don't appear in the screenshots.
  * On Linux, you can use your browsers simultaneously with a separate user.
  * The separate account can be unprivileged (no Administrator permissions).

Here's how:

## On Linux ##

Create an unprivileged user account. You can use any name that you like. Then login as that user. The -X is for X11 forwarding, so that you can start browsers without a VNC server too.

```
$ sudo adduser shotfactory1
$ ssh -X shotfactory1@localhost
```

Install the shotfactory source code (both versions 0.3 and 0.4 are shown below):

```
$ svn checkout http://svn.browsershots.org/trunk/shotfactory
$ svn checkout http://svn.browsershots.org/branches/shotfactory-django
```

Then go into the source code directory and run the ShotFactory from there:

```
$ cd shotfactory # (or shotfactory-django for 0.4)
$ python shotfactory.py -h # Show help screen
$ screen -L python shotfactory.py
```

The **screen** command will create a virtual terminal that keeps running even when you log out. The **-L** creates a logfile, usually **screenlog.0** with the complete output (in addition to the normal **shotfactory.log** with error messages).

You can close the screen with **Ctrl-A Ctrl-D** and later run **screen -rd** to connect to it again.