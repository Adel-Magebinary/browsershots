**Disclaimer: All information on this page is provided AS IS and without any warranty. I've been striving for accuracy, but there may be severe errors in this page. Fiddling with hard drives can have disastrous effects. Please be careful and always have backups.**

It's a good idea to run a RAID (Redundant Array of Independent Disks) on the central server for performance and data integrity. The server at browsershots.org has a hardware RAID-1 with a 8006-2LP controller from 3ware. Here's a loose collection of tricks for RAID maintenance.

## smartmontools ##

```
$ sudo apt-get install smartmontools
$ sudo mknod /dev/twe0 u 164 0
```

Configuration lines in **/etc/smartd.conf**:

```
# Monitor 2 ATA disks connected to a 3ware 6/7/8000 controller which uses
# the 3w-xxxx driver. Start long self-tests on Saturday and Sunday.
/dev/twe0 -d 3ware,0 -a -s L/../../6/01
/dev/twe0 -d 3ware,1 -a -s L/../../7/01
```

## tw\_cli ##

A proprietary command line tool for 3ware RAID controllers can be downloaded from http://www.3ware.com/support/download.asp.

Sometimes I get SMARTD errors from the weekly selftest:

```
$ sudo smartctl -q errorsonly -l selftest -d 3ware,1 /dev/twe0
Num  Test_Description    Status                  Remaining  LifeTime(hours)  LBA_of_first_error
# 1  Extended offline    Completed: read failure       40%      8771         10826523
```

In this case, it helps to run the following:

```
$ sudo ./tw_cli /c0/u0 start verify
```

The verify and repair procedure can take several hours. You can monitor its progress:

```
$ sudo ./tw_cli /c0 show

Unit  UnitType  Status         %Cmpl  Stripe  Size(GB)  Cache  AVerify  IgnECC
------------------------------------------------------------------------------
u0    RAID-1    INITIALIZING   79     -       152.669   ON     -        -        

Port   Status           Unit   Size        Blocks        Serial
---------------------------------------------------------------
p0     OK               u0     152.67 GB   320173056     L41LB68G            
p1     OK               u0     152.67 GB   320173056     L308BKBH            
```

After the verify, you may get the following:

```
$ sudo ./tw_cli /c0 show

Unit  UnitType  Status         %Cmpl  Stripe  Size(GB)  Cache  AVerify  IgnECC
------------------------------------------------------------------------------
u0    RAID-1    DEGRADED       -      -       152.669   ON     -        -        

Port   Status           Unit   Size        Blocks        Serial
---------------------------------------------------------------
p0     OK               u0     152.67 GB   320173056     L41LB68G            
p1     DEGRADED         u0     152.67 GB   320173056     L308BKBH            
```

When that happens, I do this:

```
$ sudo ./tw_cli maint remove c0 p1
Exporting port /c0/p1 ... Done.

$ sudo ./tw_cli info c0

Unit  UnitType  Status         %Cmpl  Stripe  Size(GB)  Cache  AVerify  IgnECC
------------------------------------------------------------------------------
u0    RAID-1    DEGRADED       -      -       152.669   ON     -        -        

Port   Status           Unit   Size        Blocks        Serial
---------------------------------------------------------------
p0     OK               u0     152.67 GB   320173056     L41LB68G            
p1     NOT-PRESENT      -      -           -             -

$ sudo ./tw_cli maint rescan 
Rescanning controller /c0 for units and drives ...Done.
Found the following unit(s): [none].
Found the following drive(s): [/c0/p1].

$ sudo ./tw_cli maint rebuild c0 u0 p1 
Sending rebuild start request to /c0/u0 on 1 disk(s) [1] ... Done.

$ sudo ./tw_cli info c0

Unit  UnitType  Status         %Cmpl  Stripe  Size(GB)  Cache  AVerify  IgnECC
------------------------------------------------------------------------------
u0    RAID-1    REBUILDING     12     -       152.669   ON     -        -        

Port   Status           Unit   Size        Blocks        Serial
---------------------------------------------------------------
p0     OK               u0     152.67 GB   320173056     L41LB68G            
p1     DEGRADED         u0     152.67 GB   320173056     L308BKBH            
```

The rebuilding makes your hard drives run much slower. In my case, the web server got too unresponsive because of slow database access. It may help to stop the web server until the rebuild is finished. I think the rebuild went faster when most other hard drive access was paused. In the end it should look like this again:

```
$ sudo ./tw_cli info c0

Unit  UnitType  Status         %Cmpl  Stripe  Size(GB)  Cache  AVerify  IgnECC
------------------------------------------------------------------------------
u0    RAID-1    OK             -      -       152.669   ON     -        -        

Port   Status           Unit   Size        Blocks        Serial
---------------------------------------------------------------
p0     OK               u0     152.67 GB   320173056     L41LB68G            
p1     OK               u0     152.67 GB   320173056     L308BKBH            
```

There's a new syntax for the commands above, and the old syntax will be removed in a future release of tw\_cli. I think these are the above commands in new syntax, but I'm just guessing from the documentation, and haven't tried these:

```
$ sudo ./tw_cli /c0/p1 export
$ sudo ./tw_cli /c0 show
$ sudo ./tw_cli /c0 rescan
$ sudo ./tw_cli /c0/u0 start rebuild disk=p1
$ sudo ./tw_cli /c0/u0 pause rebuild
$ sudo ./tw_cli /c0/u0 resume rebuild
```

After a successful rebuild, you should run a long selftest on the drive. This takes several hours as well, but it doesn't affect the server performance as heavily as the rebuild. The two lines in **/etc/smartd.conf** near the top of this page schedule the same test for every weekend.

```
$ sudo smartctl --test=long -d 3ware,1 /dev/twe0
$ sudo smartctl --all -d 3ware,1 /dev/twe0 | grep -B1 remaining
$ sudo smartctl --log=selftest -d 3ware,1 /dev/twe0
Num  Test_Description    Status                  Remaining  LifeTime(hours)  LBA_of_first_error
# 1  Extended offline    Completed without error       00%      8910         -
# 2  Extended offline    Aborted by host               40%      8902         -
# 3  Extended offline    Completed: read failure       40%      8771         10826523
...
#19  Extended offline    Completed without error       00%      6103         -
#20  Short offline       Completed without error       00%         0         -
```