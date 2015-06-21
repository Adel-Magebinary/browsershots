**This page is still incomplete.**


---


## Hardware and OS ##

See RequirementsForServer.


---


## ShotServer ##

### Get the source code ###

You can download the source code from http://download.browsershots.org/releases/ and then unzip it.

Or you can use Subversion to check out the latest development version of the software (which is running on browsershots.org):

```
svn checkout https://svn.browsershots.org/trunk/shotserver
```

### Install the software ###

```
cd shotserver
sudo python setup.py install
sudo apache2ctl restart
```


---


## Apache ##

### Apache installation ###

```
sudo apt-get install apache2 libapache2-mod-python netpbm
```

### SSL configuration ###

If you want to use SSL (HTTPS) for password security, you need to generate a SSL certificate:

```
sudo apache2-ssl-certificate -days 365
```

... and include port 443 in **/etc/apache2/ports.conf**:

```
Listen 80
Listen 443
```

... and also enable the SSL module in Apache:

```
sudo a2enmod ssl
```

### Site configuration ###

Then you copy the configuration files from the source code. Ignore the file with **-ssl** if you don't use SSL.

```
cd shotserver
sudo cp conf/browsershots.org /etc/apache2/sites-available/
sudo cp conf/browsershots.org-ssl /etc/apache2/sites-available/
```

You will have to adapt them to your local server configuration, especially the hostname. It is recommended to rename the files to reflect the actual hostname of your server. The browsershots server can be run on the same machine with other sites, using name-based virtual hosts. In the file **/etc/apache2/sites-available/default** you may have to add the port number, like this:

```
NameVirtualHost *:80
<VirtualHost *:80>
```

### Create folders and content ###

If you haven't changed the directories in the config files, you must create the following folders:

```
sudo mkdir /var/log/apache2/browsershots.org
sudo mkdir /var/www/browsershots.org
sudo ln -s /usr/share/shotserver03/style /var/www/browsershots.org/style
```

### Enable modules and sites ###

Then enable some necessary modules, and the new sites (replace browsershots.org with the names of your site configuration files).

```
sudo a2enmod rewrite
sudo a2ensite browsershots.org
sudo a2ensite browsershots.org-ssl
sudo apache2ctl restart
```


---


## Database ##

### PostgreSQL installation ###

```
sudo apt-get install postgresql-8.1
```

### Create the database ###

The database should be owned by the user that the web server runs under (www-data on Debian and Debian-based distros like Ubuntu). To create a new database, you can use

```
scripts/shotserver03_db_drop_create.sh
```

or run the following commands manually:

```
echo 'CREATE USER "www-data"' | sudo su - postgres psql template1
echo 'CREATE DATABASE shotserver03' | sudo su - postgres psql template1
echo 'GRANT ALL PRIVILEGES ON DATABASE shotserver03 TO "www-data"' | sudo su - postgres psql shotserver03
cat sql/create_tables.sql | sudo su - www-data psql shotserver03
```

### Create screenshot factories ###

To work directly with the database, you should become the user www-data:

```
sudo su - www-data psql shotserver03
```

In the database client console, you can then create database rows like this:

```
INSERT INTO person (nickname, name, email, salt, password) VALUES ('joe', 'Joe Schmoe', 'joe@example.com', 'af09', MD5('af09secret'));
INSERT INTO architecture (name, creator) VALUES ('i386', 1);
INSERT INTO opsys_group (name, creator) VALUES ('Linux', 1);
INSERT INTO opsys_group (name, manufacturer, creator) VALUES ('Mac OS', 'Apple', 1);
INSERT INTO opsys_group (name, manufacturer, creator) VALUES ('Windows', 'Microsoft', 1);
INSERT INTO opsys (opsys_group, distro, codename, major, minor, creator) VALUES (1, 'Ubuntu', 'Edgy', 6, 10, 1);
INSERT INTO factory (name, owner, creator, opsys, architecture) VALUES ('edgybox', 1, 1, 1, 1);
INSERT INTO factory_screen VALUES (1, 800, 600);
INSERT INTO factory_screen VALUES (1, 1024, 768);
INSERT INTO factory_feature VALUES (1, 'bpp', 8);
INSERT INTO factory_feature VALUES (1, 'bpp', 16);
INSERT INTO factory_feature VALUES (1, 'bpp', 24);
INSERT INTO factory_feature VALUES (1, 'js', NULL, 'yes');
INSERT INTO factory_feature VALUES (1, 'java', NULL, 'yes');
INSERT INTO factory_feature VALUES (1, 'flash', NULL, 'yes');
```