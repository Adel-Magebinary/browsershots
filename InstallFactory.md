Specific instructions for all supported platforms:

  * InstallFactoryLinux
  * InstallFactoryWindows
  * InstallFactoryMac

## Register your factory ##

  * If you don't have a password yet, please [create a user account](https://browsershots.org/accounts/email/).
  * If you get an error saying **Factory not found with name=...**, please [register your screenshot factory](https://browsershots.org/factories/add/).
  * If you get **No browsers registered for factory ...**, please visit [this page](https://browsershots.org/browsers/add/) with each of your browsers.

## Troubleshooting ##

  * Run **shotfactory.py -h** (or **--help**) to see a list of command line options.
  * Run **shotfactory.py -v** (or **--verbose**) to see more output, including error messages from helper programs.
  * Run **shotfactory.py -vvv** (very very verbose) to also see all the commands that are run by the script.
  * On Linux, you can run **xvncviewer :1** to see the virtual screen of the VNC server while a screenshot request is processed.
  * You can also look at the files **????-pgdn01.ppm** or **????.png** (where ???? is the request number) to see if there's a problem.
  * The file **shotfactory.log** contains error messages for failed screenshot requests.
  * If you use **screen -L**, the file **screenlog.0** will contain the full output of the shotfactory script.
  * On Windows, if you run **shotfactory.exe** directly with a double click, the terminal window may be closed immediately when an error occurs. Try to start the terminal first and then run the program from the command line to avoid this issue.
  * The [factory details page](http://browsershots.org/factories) shows recent errors for your factory, with links to each screenshot.
  * The FactoryErrors page explains the factory error numbers with some hints how to fix them.
  * The FrequentlyAskedQuestions#Runningascreenshotfactory page has a section with specific factory errors too.