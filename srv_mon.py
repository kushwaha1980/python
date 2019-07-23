import os, datetime, time
from datetime import date, timedelta

tsm = '/usr/tivoli/tsm/client/ba/bin64/dsmc sched'

host = os.popen("hostname").read().strip()
print("------------------------------Segment-Start- " + host + "-------------------------------")
up = os.popen("uptime|awk '{print $2, $3, $4}'").read()
sar = os.popen("sudo sar 2 4|grep -i ave").read().split()

print("The System uptime is: " + up)
print("The Load Average, %usr: " + sar[1] + " %sys: " + sar[2] + " %idle: " + sar[4])

print("-------------------------------------------------------------")
if os.path.isdir("/usr/tivoli/tsm/client/ba/bin64") or os.path.isdir("/usr/tivoli/tsm/client/ba/bin"):
        proc = os.popen("ps -Af").read()
        if tsm in proc:
                tsmdate = os.popen("sudo dsmc q fi|grep -i jfs2|head -1|awk '{print $2}'").read()
                print "TSM process is running and last backup date is: " + tsmdate,
        else:
                print("TSM backup is NOT running, please TROUBLESHOOT the issue!!!")

if os.path.isdir("/usr/openv/netbackup/bin"):
        netb = Popen(["/usr/openv/netbackup/bin/bpclimagelist|head -3"], stdout = PIPE, shell = True)
        for line in netb.stdout:
                if line.startswith("Backed"):
                        continue
                if line.startswith("-"):
                        continue

                line = line.split()
        print("the last NET BACKUP happend on: %s " % line[0])
print("-------------------------------------------------------------")

print("---------------------------------------------------------------")
d = datetime.datetime.now()

errpt = os.popen("errpt|head").read()
num = os.popen("errpt|head|awk '{print $2}'").read().split("\n")

d1 = d.strftime("%m")+ d.strftime("%d")
yest = date.today() - timedelta(1)
dyest = date.today() - timedelta(2)
d2 = yest.strftime("%m%d")
d3 = dyest.strftime("%m%d")
list = []

for i in errpt.split("\n"):
        if i.startswith("IDENTIFIER"):
                continue
        if i.startswith("A924A5FC"):
                continue
        list.append(i)

if any((d1 or d2 or d3) in n for n in num[:]):
        for line in list:
                if d1 or d2 or d3 in list:
                        print(line)
else:
        print ("All looks Good.....No error from last 3 days")
print("------------------------------Segment-End-" + host + "---------------------------------")
