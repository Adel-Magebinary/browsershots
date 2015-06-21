## Server scalability ##

  * Move database server to separate machine
    * db.browsershots.org
  * Move PNG files to separate machine
    * screenshots.browsershots.org for screenshots
    * xmlrpc.browsershots.org for FactoryInterface
  * Move trac.browsershots.org to a separate machine
    * Separate database server for Trac (maybe sqlite)
    * svn.browsershots.org on same machine maybe
    * lists.browsershots.org on same machine maybe
  * Load balancing among multiple web servers
    * browsershots.org
    * ssl.browsershots.org