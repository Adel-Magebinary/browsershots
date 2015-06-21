# 204 #

## No matching request. ##

There weren't any screenshot requests that match your factory configuration. The factory should sleep for a minute and then poll again.

## All active browsers on ??? are temporarily blocked because of errors. ##

When a screenshot upload contains errors, the respective browser will be blocked for 10 minutes to reduce the number of errors per hour, and to give other factories a chance to process this request. If all browsers on your factory have errors, request polling will fail until the first browser is unblocked again.


---


# 401 #

## Authentication failed (different IP address). ##

The IP address of your screenshot factory has changed after the XML-RPC call to [nonces.challenge](http://api.browsershots.org/xmlrpc/nonces.challenge/). Maybe it is using a different proxy server. For security, the factory must use the same IP address for the challenge and the subsequent API call.

# 404 #

## No active browsers registered for factory ???. ##

Please visit the [browser registration page](http://browsershots.org/browsers/add/) with each of the browsers that you want to run on your factory.

## Unknown user agent: ... ##

Your browser was probably updated, and the user agent has changed. Visit the [browser registration page](http://browsershots.org/browsers/add/) again with this browser to update the user agent string in the database.

# 406 #

## The browser has not visited the requested website. ##

Actually, the browser has not visited the redirect address on the Browsershots server. Maybe another instance of this browser is running, and the uploaded screenshot contains an error message about it. Or maybe your browser didn't have enough time to start up and load the requested page, so you may try to increase the value of the `--wait` option (default is 30 seconds).

# 408 #

## Authentication failed (nonce expired). ##

The delay between the XML-RPC call to [nonces.challenge](http://api.browsershots.org/xmlrpc/nonces.challenge/) and the subsequent API call was longer than 10 minutes. Maybe your screenshot factory is too busy with other work (like a software upgrade), or your internet connection is too slow.

# 409 #

## Requested browser version ?.? but got ?.?. ##

Your screenshot factory has started the wrong browser for this screenshot request. Visit the [browser registration page](http://browsershots.org/browsers/add/) with each browser and enter the correct filename in the **Command** field.

## Request ??? was not locked. ##

Your screenshot factory has tried to upload a screenshot for a request that wasn't locked. Locking should happen during the call to [requests.poll](http://api.browsershots.org/xmlrpc/requests.poll/). This is probably a programming error in the shotfactory script or the server.

# 412 #

## The screenshot is ??? pixels wide, not ??? as requested. ##

Make sure that you have `reschangecon.exe` (on Windows) or `cscreen` (on Mac OS) to adjust your screen resolution. Or if the requested screen resolution is not supported on your factory, you can remove it on the factory page (you have to log in to see the buttons).

# 413 #

## The screenshot is too tall (more than 4 times the width). ##

Extremely tall screenshots break the page layout on browsershots.org, and they use up a lot of disk space on the server without much benefit. Please reduce your vertical screen resolution, or the value of the `--max-pages` option (the default is 7).

# 414 #

## The screenshot is too short (less than half the width). ##

If your screen resolution is really wider than 2:1, please write to [johann@browsershots.org](mailto:johann@browsershots.org) so I can change the limit.

# 415 #

## Could not decode uploaded PNG file (hashkey ???). ##

Your screenshot factory uploaded a PNG file that could not be decoded. Please write to [johann@browsershots.org](mailto:johann@browsershots.org) with details on your software installation (e.g. operating system, installed version of NetPBM).

# 423 #

## Request ??? was locked by factory ???. ##

Your screenshot factory took longer than 5 minutes to process the screenshot request, so the lock expired and a different factory started to process this request.


---


# 503 #

## The server is currently overloaded. Please try again in a minute. ##

If the server load average (from `/proc/loadavg`) exceeds 10, some calls to [requests.poll](http://api.browsershots.org/xmlrpc/requests.poll/) will be randomly rejected to reduce the server load. If the load goes higher, more polls will be rejected. The screenshot factory should sleep for a minute and then try to poll for a screenshot request again.


---


# 601 #

## Internet Explorer has encountered a problem ##

This problem occurs because one of the following browser helper objects (BHO) is installed on your computer: Buyersport, Morpheus, Morpheus Shopping Club, WURLD Shopping Community. Additionally, you logged on to the computer with a limited user account. The BHO tries to modify certain system files and Windows Registry entries that require administrative credentials to access. As a result, when the BHO cannot access these files and registry entries, Internet Explorer stops abruptly. To resolve this problem, remove the BHO from your computer. More information is available in the [Microsoft Knowledge Base](http://support.microsoft.com/kb/827315/EN-US/).

# 602 #

## Send Error Report ##

The browser processing the current screenshot request crashed and Application Error Reporting is enabled in Windows system settings. To resolve this error, either disable Application Error Reporting (System Properties, Advanced), or, better, find out why the browser crashed while attempting to load the particularly requested website.

# 603 #

## Low virtual memory ##

Your system does not have enough free [RAM](http://en.wikipedia.org/wiki/RAM) to continue service. This takes place when the system is overloaded or executing external programs, such as a web server, while the shotfactory is running. For first, try to restart the operating system in order to free unused memory. If the issue is not solved by this, start Task Manager (Ctrl-Shift-Esc), and keep it running minimized. After the error occured the next time, open task manager, have a look at the 'Processes' tab and thus find out which program is consuming most memory.

# 631 #

## Install language pack ##

The requested website contains characters that cannot be shown with the language packs currently installed. Usually, this causes Internet Explorer to display a dialog box requesting the on-demand install of additional codepages. The needed packs are often Chinese, Japanese, and other Eastern language packs. Once the additional pack has been installed, make sure to restart the browser to complete the setup. Sometimes even the whole operating system must be restarted. Note: installing language packs requires Administrator privileges. Firefox does not show a dialog asking for on-demand setup, but rather only shows boxes containing the hexadecimal unicode values of the signs not available. A good website to test if Eastern signs are displayed correctly is [Toshiba](http://www.toshiba.co.jp/).

# 651 #

## You have requested an encrypted page ##

This is not a warning but rather a message telling you that the currently requested website is using the secure SSL protocol. Please be sure to disable such messages in the preferences of your browser in order to hide them from made screenshots.

# 652 #

## Secure connection ##

This is not a warning but rather a message telling you that the currently requested website is using the secure SSL protocol. Please be sure to disable such messages in the Internet options of Internet Explorer in order to hide them from made screenshots.

# 671 #

## Waiting for http ##

This message indicates that the page could not be loaded in the given wait time. To resolve this problem, first try to open the URL in your normal browser on your desktop computer. Wait some 30 seconds or even longer. If the page loads, increase the wait timeout in the shotfactory (-w parameter). If it does not load, try opening any website on the shotfactory computer. If that works the web server of the requested website is not available and you cannot do anything against the error message as the administrator of the webserver is responsible. If you cannot open any page on your shotfactory computer, there is an error with your internet connection there.

# 681 #

## Do not show this warning again ##

Several dialog messages and warnings contain a checkbox to hide such messages in the future. Check the box once to remove the dialogs. This message is also displayed by Internet Explorer if you set the accepting of cookies to 'Confirm' instead of 'Accept' or 'Block'.

# 692 #

## Recycle Bin ##

Your screenshot contains the Recycle Bin desktop icon; the requested browser did thus not start in maximized window state. Try to maximize it once, then close it. Most browsers then save your window state preference for the next start. Note: you must close the browser manually after maximizing the window as the shotfactory will not close it softly, but kill the process.

# 693 #

## Server poll latency ##

Your screenshot contains the open console window with the shotfactory debug output. Try minimizing the console window, and make sure all browsers can start in the given wait time. If they can't, increase the wait time, using the -w parameter.


---


# 701 #

## The screen is blank ##

Automatically detected error within the screenshot, showing that most of your screen was blank. Usually refers to a browser not being maximized or not having loaded the page fully.

# 702 #

## The left side of the screen is blank ##

Automatically detected error within the screenshot, showing that the left side of your screen was blank. Usually refers to a browser not being maximized or not having loaded the page fully.

# 703 #

## The right side of the screen is blank ##

Automatically detected error within the screenshot, showing that the right side of your screen was blank. Usually refers to a browser not being maximized or not having loaded the page fully.

# 704 #

## The bottom of the screen is blank ##

Automatically detected error within the screenshot, showing that the bottom of your screen was blank. Usually refers to a browser not being maximized or not having loaded the page fully.

This also happens in Safari if there's no scroll bar and the bottom of the website is blank. In that case, you can avoid this error by enabling the status bar in Safari.


---


# 811 #

## This is not the requested browser. / This is not ???. ##

User-reported error telling you that the shot screenshot does not contain the browser requested for this screenshot. Usually refers either to wrong entries within the section 'Registered browsers for this shotfactory' or to wrong program paths / exe calls.

# 812 #

## This is not the requested operating system. / This is not ???. ##

User-reported error telling you that the shot screenshot was not recorded in the operating system requested for this screenshot. Please check your registered browsers and compare them to the ones installed in the shotfactory computer.

# 821 #

## This is not the requested Javascript version. / Javascript is not ?.?. ##

Indicates that the screenshot requested a different Javascript version than the one used in the recorded browser. You will have to compare the settings within your Browsershots account to the real Javascript version used in the browser, and update the setting, if needed.