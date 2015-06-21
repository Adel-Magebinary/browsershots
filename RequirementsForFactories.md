Screenshot factories are the machines that run a fully automatic unattended script to get jobs from the server and make screenshots of browsers.

**Hardware:** I run several screenshot factories on Pentium III machines with 500 MHz and 256MB of RAM. That seems to be quite sufficient. On Linux, the browsers run in a VNC server, so you don't need any graphics hardware on the screenshot factory machine.

**Software:** The reference implementation requires the following software.

  * [Python](http://www.python.org/) (tested with version 2.3 to 2.5)
  * On Linux: VNC server (for example [TightVNC](http://www.tightvnc.com/)), [Netpbm](http://netpbm.sourceforge.net/) graphic software, [xautomation](http://hoopajoo.net/projects/xautomation.html) utilities
  * On Windows: [Python Win32 API](http://www.python.net/crew/mhammond/win32/), [Python Imaging Library](http://www.pythonware.com/products/pil/), [Resolution Changer](http://www.12noon.com/reschange.htm), [Process Viewer](http://www.teamcti.com/pview/prcview.htm)
  * On Mac: [NetPBM tools](http://netpbm.sourceforge.net/), [cscreen](http://www.versiontracker.com/dyn/moreinfo/macosx/19753) ([mirror](http://download.browsershots.org/thirdparty/cscreen.dmg)), [appscript](http://appscript.sourceforge.net/download.html)

If Python is not available for your platform, you could write your own screenshot factory script in your favorite programming language, according to the FactoryInterface specification.

**Interface:** The screenshot factories communicate with the central server through XML-RPC which is based on HTTP. The FactoryInterface protocol will also work through most firewalls and even through web proxies.

**Bandwidth:** One screenshot factory can process about one screenshot per minute. Screenshots are in PNG format for lossless compression. For screens with low resolution (800x600 pixels) and few colors (e.g. 256), the average screenshot size is somewhere around 50 kilobytes. On slightly more modern platforms (1024x768 pixels and 24 bits per pixel), a single screenshot can be as large as half a megabyte. This can amount to 30 megabytes per hour or 720 megabytes in 24 hours. Therefore, the monthly upload bandwidth usage of a single screenshot factory can be in the order of 20 gigabytes.

**CPU usage:** This depends on the browser and website (e.g. Flash and/or Java). For a busy factory, the CPU usage would average 20% to 50% on a modern computer, but the usage would occur in bursts during the start of the VNC server, during page loading and rendering, and during PNG encoding.

**Load limit:** On Linux and Mac, you can specify a load limit, the default value is 1.0. If the system load average exceeds the limit, the screenshot factory program will sleep until the load goes down.

**Parallel factories:** If one machine runs several screenshot factories in parallel, the bandwidth and CPU usage must be multiplied by the number of parallel factories.