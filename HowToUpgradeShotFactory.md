There are two different methods of upgrading your screenshot factory, depending on how you installed it initially.

[[PageOutline(2,,inline)]]

Starting with milestone:0.3-beta1, the system-wide installation with **python setup.py install** is no longer required.

## Upgrading the source code from Subversion ##

If you're running a ShotFactory with the source code from Subversion, upgrade your installation as follows.

  * Open a terminal window and **cd** into the shotfactory folder.
  * Type **svn update** and press Enter.

## Upgrading from a zip file release ##

If you're running a ShotFactory with the source code of a previous release (from a zip file) or with the binary files (including shotfactory.exe), upgrade your installation as follows.

  * Rename your old shotfactory folder.
  * Download the [latest source release](http://download.browsershots.org/releases) (or [binary archive](http://download.browsershots.org/binaries/)) and unzip it.
  * If you get two folders named **shotfactory-![r977](https://code.google.com/p/browsershots/source/detail?r=977)-win32** (one inside the other), move the inner folder up a level.
  * Rename the new folder from **shotfactory-![r977](https://code.google.com/p/browsershots/source/detail?r=977)-win32** to **shotfactory**.
  * If you have any stand-alone browser subdirectories (e.g. IE55SP2\_NT), move them from the old shotfactory folder to the new one.