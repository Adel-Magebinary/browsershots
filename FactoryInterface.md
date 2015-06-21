This is the specification for the interface between the central server and the distributed screenshot factories.

[The central server](ShotServer.md) is a web server with a big fat pipe.

[The screenshot factories](ShotFactory.md) are simple workstations with cheap broadband internet access (e.g. DSL or cable). They communicate with the server by means of XML-RPC (Remote Procedure Call). This works fine with firewalls and proxies because it's like regular web surfing (except for the frequency and size of file uploads).

The screenshot factory program is a simple script that runs fully unattended. It downloads job information from the central server, runs a web browser and produces screenshots, and finally uploads the resulting PNG files to the central server.

The XML-RPC endpoint is at http://api.browsershots.org/xmlrpc/. The API documentation is available on the same URL, simply go there with your browser.

## Step 0: Authentication ##

Get a challenge from the server and encrypt your password for each API request.

http://api.browsershots.org/xmlrpc/nonces.challenge/

## Step 1: Get a screenshot request ##

Ask the server to find a screenshot request that matches your factory configuration, and lock it (to avoid that two screenshot factories work on the same request).

http://api.browsershots.org/xmlrpc/requests.poll/

The result includes a request ID, the browser name and version number, and other request details.

## Step 2: Make a screenshot ##

Set up the screen to match the request parameters, e.g. resolution and color depth.

Construct a redirection URL:

  * http://api_server_name/redirect/factory_name/encrypted_password/request_id/
  * http://api.browsershots.org/redirect/argo/0c17c0414b6afc738c32cc5576fceaf6/3802921/

Start your browser with the redirection URL. The central server will store the User-Agent header of your browser and then redirect the browser to the URL for the job, using the status code '302 Found'.

Now you have to wait until the browser has finished rendering the page. Then take a screenshot of the whole screen, including window decorations and task bar.

Optionally scroll down, take more screenshots, and merge the screenshots into a tall picture.

## Step 3: Upload PNG file ##

Make a PNG file from the screenshot. Encode it to **base64** and send it to the server.

http://api.browsershots.org/xmlrpc/screenshots.upload/

The central server will sanity-check your submission, then make smaller images and store the PNG files on disk. Users can see their screenshots at the following URL: http://browsershots.org/screenshots/

You can now go back to step 1 and check for more jobs.

If you don't want to produce too much load on your host, you can wait until your CPU load average has dropped below some limit. On Linux, this can be done by monitoring /proc/loadavg until the first number is below 1.0 or something.