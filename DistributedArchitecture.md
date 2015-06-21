## 1. System Components ##

The Browsershots system consists of a central server and a large number of distributed screenshot factories.

ShotServer: The central server is a powerful web server. It has a web interface that consists of a user interface and a configuration area. The server manages the screenshot requests, uploaded screenshots, and the configuration of the factories.

ShotFactory: The screenshot factories are simple desktop machines with cheap broadband internet. They make screenshots of web pages in different browsers on different platforms. Some of them are only active at night or when they have nothing else to do. The screenshot factory program is fully automatic and runs completely unattended.

## 2. Life Cycle of a Screenshot Request ##

Users submit their web addresses to the central server through a web-based user interface. Then they select browsers and configuration options for their screenshots. The screenshot requests are stored in a database on the central server.

FactoryInterface: The screenshot factories poll the server regularly for requests that match their configuration. If a matching screenshot request is found, the factory loads the requested page in the requested browser and makes screenshots of it. If the page is longer than one screen, several screenshots will be merged to produce a tall picture of the whole page. Finally, the screenshot is compressed as a PNG file and uploaded to the central server.

A few minutes after the screenshot requests were submitted, users can see the results in their browser on the central server's web interface.