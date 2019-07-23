#!/usr/bin/python
import paramiko, os, sys

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("server_name", port = 22)

stdin, stdout, stderr = ssh.exec_command("/home/user_name/srv_mon.py")

stdin.write("y")
stdin.write("\n")
stdin.flush()

opt = stdout.readlines()
print "\n".join(opt)
ssh.close()
