The machine at http://browsershots.org/ is an example of a central server for the Browsershots system. If you want, you can set up your own server and use it for private screenshots in your web design company, for example.

**Hardware:** The current server for browsershots.org is 3 separate VMware systems with 5 CPUs, 6 GB RAM, 400 GB disk space, sponsored by [QuickHost.com](http://www.quickhost.com/). For smaller loads (e.g. in-house use), a half-modern web server with 512 MB RAM and 40 GB HD should be okay.

**Software:** I run Ubuntu 6.06 and Apache 2. The Shotserver is written in Python and requires the mod\_python module for Apache 2. It also needs some imaging tools from the netpbm package to unpack PNG files and produce smaller previews.

**Bandwidth:** For the server, the bandwidth requirements must be multiplied by the number of screenshot factories. If there are 20 active factories at any time, the bandwidth for screenshot uploads alone will have to be in the order of half a terabyte per month.

**Storage:** Hard drive usage for screenshots is quite flexible because when the disk gets filled up, old screenshots can be deleted automatically with a cron job.