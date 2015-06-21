The ShotFactory is a python script that runs on the distibuted screenshot factories. Here is what it does:

  * Poll the ShotServer for a job.
  * Launch a browser, load the job page.
  * Make a multi-page screenshot of the browser.
  * Upload the resulting PNG file to the ShotServer.

See DistributedArchitecture for an overview of the system.