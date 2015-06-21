This page has been updated to work with Browsershots 0.4.

## Install prerequisites ##

```
sudo apt-get install tightvncserver xfonts-base netpbm xautomation scrot subversion
```

## Get the screenshot factory source code ##

```
svn checkout http://svn.browsershots.org/trunk/shotfactory/
```

## Adjust config files ##

Change the file **~/.vnc/xstartup** to the following three lines. This will set a white background and then run nothing except the window manager. Be sure to remove any reference to xterm because it gets in the way. If you have never run **tightvncserver** before, this file will not yet exist - run it once to automatically generate the file, and then make the change.

```
#!/bin/sh
xsetroot -solid "#FFFFFF"
x-window-manager &
```

If the file doesn't have any effect, make sure it's executable:

```
chmod a+x ~/.vnc/xstartup
```

## Run ##

```
cd shotfactory
screen -L python shotfactory.py
```

See InstallFactory for registration and troubleshooting tips.

## More useful packages ##

You will want to run a lightweight window manager because it will be restarted for each screenshot request. I don't recommend **gnome-session** because it uses a lot of memory. If you want nice rounded title bars, you can also install **ubuntu-artwork**.

```
sudo apt-get install metacity ubuntu-artwork
```

The firefox package on Ubuntu suggests these font packages (as of 2007-12-01):

```
sudo apt-get install latex-xft-fonts ttf-kochi-gothic ttf-kochi-mincho ttf-thryomanes ttf-baekmuk ttf-arphic-gbsn00lp ttf-arphic-bsmi00lp ttf-arphic-gkai00mp ttf-arphic-bkai00mp
```

If you want to run Flash 9, simply install the following package:

```
sudo apt-get install flashplugin-nonfree
```

It's also fun to track the system status graphically. Install [Munin](http://munin.projects.linpro.no/) somewhere and add all your screenshot factory machines to **/etc/munin/munin.conf**. Then do this on each screenshot factory:

```
sudo apt-get install lm-sensors smartmontools
sudo apt-get install munin-node
```