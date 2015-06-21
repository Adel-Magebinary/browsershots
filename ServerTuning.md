Increase PostgreSQL connection limit:

```
#!diff
--- /etc/postgresql/8.3/main/postgresql.conf    2008-10-15 19:05:17 +0000
+++ /etc/postgresql/8.3/main/postgresql.conf    2008-10-20 00:34:44 +0000
@@ -58,7 +58,7 @@
                                        # defaults to 'localhost', '*' = all
                                        # (change requires restart)
 port = 5432                            # (change requires restart)
-max_connections = 100                  # (change requires restart)
+max_connections = 400                  # (change requires restart)
 # Note:  Increasing max_connections costs ~400 bytes of shared memory per 
 # connection slot, plus lock space (see max_locks_per_transaction).  You might
 # also need to raise shared_buffers to support more connections.
@@ -104,7 +104,7 @@
 
 # - Memory -
 
-shared_buffers = 24MB                  # min 128kB or max_connections*16kB
+shared_buffers = 200MB                 # min 128kB or max_connections*16kB
                                        # (change requires restart)
 #temp_buffers = 8MB                    # min 800kB
 #max_prepared_transactions = 5         # can be 0 or more
@@ -117,7 +117,7 @@
 
 # - Free Space Map -
 
-max_fsm_pages = 153600                 # min max_fsm_relations*16, 6 bytes each
+max_fsm_pages = 500000                 # min max_fsm_relations*16, 6 bytes each
                                        # (change requires restart)
 #max_fsm_relations = 1000              # min 100, ~70 bytes each
                                        # (change requires restart)
```

Increase kernel shared memory from 32MB to 256MB:

```
sudo sysctl -w kernel.shmmax=268435456
```

Store setting for next reboot:

```
#!diff
--- /etc/sysctl.conf    2008-10-15 19:05:17 +0000
+++ /etc/sysctl.conf    2008-10-20 00:32:54 +0000
@@ -74,3 +74,6 @@
 #net/ipv4/ip_always_defrag = 1
 net.ipv4.tcp_syncookies = 1
 net.ipv4.tcp_synack_retries = 2
+
+# Increase SHMMAX for PostgreSQL to 256 MB
+kernel.shmmax = 268435456
```

Reduce KeepAliveTimeout and increase MaxClients for Apache:

```
#!diff
--- apache2/apache2.conf        2008-10-15 19:05:17 +0000
+++ apache2/apache2.conf        2008-10-20 01:00:58 +0000
@@ -87,7 +87,7 @@
 # KeepAliveTimeout: Number of seconds to wait for the next request from the
 # same client on the same connection.
 #
-KeepAliveTimeout 15
+KeepAliveTimeout 5
 
 ##
 ## Server-Pool Size Regulation (MPM specific)
@@ -116,9 +116,9 @@
 # MaxRequestsPerChild: maximum number of requests a server process serves
 <IfModule mpm_worker_module>
     StartServers          2
-    MaxClients          150
+    MaxClients          400
     MinSpareThreads      25
     MaxSpareThreads      75
     ThreadsPerChild      25
     MaxRequestsPerChild   0
 </IfModule>
```