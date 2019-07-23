#!/usr/bin/python

#This script take user input from jump server when remote server script is being excuted.

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("server_name", port = 22)
channel = ssh.invoke_shell()
channel_data = str()
input = str()


while True:
   if channel.recv_ready():
      channel_data = channel.recv(9999)
      print channel_data,
   elif input in ("y", "n") and channel_data.startswith("[user_name@server_name]</home/user_name>"):
      break
   else:
      continue

   if channel_data.startswith("[user_name@server_name]</home/user_name>"):
      channel.send("/home/user_name/srv_mon.py\n")
   elif channel_data.startswith("Seems the TSM process"):
      input = raw_input("\n\n\t Seems the TSM process is NOT running.Would like try to start it ? y/n:")
      channel.send(input)
      channel.send("\n")
channel.close()
ssh.close()

