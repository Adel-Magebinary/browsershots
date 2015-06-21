This pages collects some notes on how the PostgreSQL database on the shotserver can be replicated with Slony-I. This lets us switch database servers with minimal downtime, since we don't have to go offline for a whole database dump/load cycle.

The information on this page was compiled from the following sources:

  * http://slony.info/documentation/firstdb.html
  * http://slony.info/documentation/adminscripts.html
  * http://www.postgresql.org/docs/8.2/static/

This configuration adds a new server (slave) that mirrors all changes from the original database server (master). The Slony-I software needs to be installed only on the slave, and the `slon` process for the master node will connect to the master database through the local network.

Install software packages on the slave:
```
sudo apt-get install postgresql-8.2-slony1 slony1-bin libdbd-pg-perl
```

The master needs only the `postgresql-8.2-slony1` package, which is only available for Gutsy (only 8.1 for Feisty), so you need to build it if you're using PostgreSQL 8.2 on Feisty. Be sure to use the matching version of slony1 (it's 1.2.9 in Gutsy).
```
sudo apt-get install build-essential flex bison postgresql-server-dev-8.2
wget http://slony.info/downloads/1.2/source/slony1-1.2.9.tar.bz2
tar xjvf slony1-1.2.9.tar.bz2
cd slony1-1.2.9/
./configure --with-pgconfigdir=/usr/lib/postgresql/8.2/bin
make
sudo make install
```

On the master and the slave, create a separate superuser for Slony-I:
```
echo "CREATE USER slony WITH PASSWORD 'slo345' SUPERUSER" | sudo -u postgres psql template1
```

On the master and slave, add access for the new `slony` user to `/etc/postgresql/8.2/main/pg_hba.conf`:
```
# Slony-I database replication
# TYPE  DATABASE        USER    CIDR-ADDRESS          METHOD
host    shotserver04    slony   216.151.162.116/32    md5
```

On the slave, create the normal database and user:
```
echo "CREATE USER johann CREATEDB" | sudo -u postgres psql template1
createdb shotserver04
```

Install pl/pgSQL procedural language on master and slave:
```
sudo -u postgres createlang plpgsql shotserver04
```

Copy database schema from master to slave:
```
pg_dump -s shotserver04 | ssh postgres@db02 psql shotserver04
```

On the slave, run the following script to generate the configuration file `/etc/slony1/slon_tools.conf`.
```
#!sh
#!/bin/sh
CONF=/etc/slony1/slon_tools.conf
cat << EOF > $CONF
\$CLUSTER_NAME = 'replication';
\$LOGDIR = '/var/log/slony1';
\$MASTERNODE = 1;
EOF
slonik_build_env \
-node db01:shotserver04:slony:slo345 \
-node db02:shotserver04:slony:slo345 >> $CONF
cat << EOF >> $CONF
\$SLONY_SETS = {
    "set1" => {
        "set_id" => 1,
        "table_id" => 1,
        "sequence_id" => 1,
        "pkeyedtables" => @PKEYEDTABLES,
        "sequences" => @SEQUENCES,
    }
}
EOF
```

You may have to change `@KEYEDTABLES` to `@PKEYEDTABLES` and replace round with square brackets for `@PKEYEDTABLES` and `@SEQUENCES` in the output of `slonik_build_env`. The `/etc/slony1/slon_tools.conf` file should look like this (tables and sequences are abbreviated here):
```
#!perl
$CLUSTER_NAME = 'replication';
$LOGDIR = '/var/log/slony1';
$MASTERNODE = 1;
&add_node(host => 'db01', dbname => 'shotserver04', port =>5432,
        user=>'slony', password=>'slo345', node=>1 );
&add_node(host => 'db02', dbname => 'shotserver04', port =>5432,
        user=>'slony', password=>'slo345', node=>2 , parent=>1);
@PKEYEDTABLES=[
        "public.auth_group",
        "public.auth_group_permissions",
        "public.auth_message",
        ...
        "public.websites_domain",
        "public.websites_website",
];
@SEQUENCES=[
        "public.auth_group_id_seq",
        "public.auth_group_permissions_id_seq",
        "public.auth_message_id_seq",
        ...
        "public.websites_domain_id_seq",
        "public.websites_website_id_seq",
];
$SLONY_SETS = {
    "set1" => {
        "set_id" => 1,
        "table_id" => 1,
        "sequence_id" => 1,
        "pkeyedtables" => @PKEYEDTABLES,
        "sequences" => @SEQUENCES,
    }
}
```

Check configuration:
```
slony_show_configuration 
```

Output should look like this:
```
Slony Configuration
-------------------------------------

Slony-I Cluster: replication
Logs stored under /var/log/slony1
Slony Binaries in: /usr/bin

Node information
--------------------------------
Node:  1 Host:       db01 User:    slony Port: 5432 Forwarding?      Parent:  0 Database: shotserver04
         DSN: host=db01 dbname=shotserver04 user=slony port=5432 password=slo345
Node:  2 Host:       db02 User:    slony Port: 5432 Forwarding?      Parent:  1 Database: shotserver04
         DSN: host=db02 dbname=shotserver04 user=slony port=5432 password=slo345
```

Uninstall previous attempts (WARNING: only if you know what you're doing):
```
slonik_uninstall_nodes | slonik
```

Initialize cluster (create `_replication` schema):
```
slonik_init_cluster | slonik
```

Start slon for both nodes (daemon and watchdog for each):
```
sudo slon_start node1
sudo slon_start node2
```

Create set (this creates the entries in the `_replication` schema):
```
slonik_create_set set1 | slonik
```

Subscribe second node to the set (this will start the replication process):
```
slonik_subscribe_set set1 node2 | slonik
```

Watch the log files to see what's going on:
```
sudo find /var/log/slony1
sudo tail -f /var/log/slony1/node2-shotserver04.log
```