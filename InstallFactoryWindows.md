**Important security notice:** don't run the screenshot factory on your Administrator account. The program will load many websites in your browser, and some of them may contain exploits for known security holes. [One of my screenshot factories has been hijacked in this way.](BlogWindowsXpFactoryTakenOverBySpyware.md) It's safest to create a new unprivileged user account and run the screenshot factory there.

See also StandaloneInternetExplorer if you want to run different versions of Internet Explorer on one machine.

There are two different ways to install the screenshot factory on windows:

[[PageOutline(2,,inline)]]

## Simple method: binaries for Windows ##

This method is strongly recommended. It does not require any other installations. Helper programs and the Python interpreter with all required libraries are included.

  * Download the latest zip file from the [binaries download section](http://download.browsershots.org/binaries/).
  * Extract the zip file somewhere (e.g. to a folder on the Desktop).
  * Double click on `shotfactory.exe`, or run it from the command line.
  * Or you can use `shotfactory.bat` which also disables the screensaver and keeps the command line window open when an error occurs.
  * To use `shotfactory.bat`, put your password in a file called `passwd.txt` in the same folder.
  * You can also create a shortcut to `shotfactory.bat` on the Desktop.

See InstallFactory for registration and troubleshooting tips.

## Advanced method: source code from the Subversion repository ##

Use this method if you want to fiddle with the source code.

  * Install the following prerequisites:
    * [Subversion](http://subversion.tigris.org/project_packages.html#windows)
    * [Python](http://www.python.org/)
    * [Python Win32 API](http://sourceforge.net/projects/pywin32/)
    * [Python Imaging Library](http://www.pythonware.com/products/pil/)
    * [Resolution Changer (Console version): reschangecon.exe](http://www.12noon.com/reschange.htm)
    * [Process Viewer (Command line version): pv.exe](http://www.teamcti.com/pview/prcview.htm)
  * Check out the latest screenshot factory source code from http://svn.browsershots.org/trunk/shotfactory/
  * Starting with milestone:0.3-beta1, global installation with **python setup.py install** is no longer required
  * Open a terminal, enter the source folder (**cd shotfactory**) and run **python shotfactory.py**
  * Make sure that **reschangecon.exe** and **pv.exe** are in the same folder where you run the script.

See InstallFactory for registration and troubleshooting tips.