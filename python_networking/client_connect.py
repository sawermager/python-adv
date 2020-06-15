#!/usr/bin/env python
""" 
Basic paramiko initialization without too many caveats. 
Beginner level.
"""
import paramiko
import pprint

# Returns a ssh client object. Note that paramiko
# can also create server objects if desired. 
client = paramiko.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Specify connectivety parameters
client.connect(
    hostname="10.215.187.82",
    username="sawermager",
    password="password"
)

"""
Paramiko makes no assumptions about what we entend to do.
This is very different from other network oriented libs, i.e., netmiko 
and napalm.
We need to specifically need to paramiko to start a new shell process
and return a connection handle. This is our handle to interact with the
network device.
"""
conn = client.invoke_shell()
conn.send("show ip interface brief\n")

# We need to manually read bytes from the connection.
output = conn.recv(65535)
pprint.pprint(output)


# We may want to convert the received bytestring into something more readable
