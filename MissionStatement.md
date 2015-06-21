**In our dreams, the web looks good for all users. So we let web designers view screenshots of their pages in different browsers, at different screen resolutions and with different plugins. We're trying to make this service easy to use, open for all (including access to the source code) and 100% free, as in free beer.**

## The problem: cross-browser incompatibilities ##

This project is concerned with a favorite problem of web designers: websites look different in other browsers. Testing a new site in many browsers can be quite time-consuming. Not everybody has a farm of legacy machines with older OSes and browsers. There are online services that offer screenshots of websites in different browsers for considerable fees. For the hobbyist and for open source projects, these fees may be prohibitive.

## The solution: community cooperation ##

The idea behind this project is to distribute the work of making browser screenshots among community members. Everybody can add URLs to the job queue on a central server. Volunteers use a small program to automatically make screenshots of web pages in their browser and upload the results to the server.

We provide a FactoryInterface specification based on XML-RPC and a reference implementation of a ShotFactory program in Python.