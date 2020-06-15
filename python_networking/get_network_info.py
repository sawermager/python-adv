#!/usr/bin/env python

"""
Brief: Demonstrate using SSH via paramiko to get information from
the network and print to screen.
"""

import time
import paramiko


def send_cmd(conn, command):
    """
    Given an open connection and a command, issue the command and wait
    1 sec for the command to be processed.

    Args:
        conn ([type]): ssh connection handle
        command ([type]): command to be execute in ssh
    """

    conn.send(command + "\n")
    time.sleep(1.0)
    
def get_ouput(conn):
    """
    Given an open connection, read all the data from the buffer and
    decode the byte string as UTF-8.

    Args:
        conn ([type]): ssh connection handle
    """
    return conn.recv(65535).decode('utf-8')

def main():
    """
    start main
    """

    # Define host inventory in line. Remember our end-point router platform types:
    # R1 is a Cisco IOS-XE CSR1000v
    # R2 is Cisco IOS-XR XRv9000
    host_dict = {
        "R1": "show running-config | section vrf_definitiion",
        "R2": "show running-config vrf",
    }

    # For each host in the inventory dict, extract key and value
    for hostname, vrf_cmd in host_dict.items():
        
        # paramiko can be ssh client or server; use client here
        conn_params = paramiko.SSHClient()
        
        # We don't need paramiko to refuse connections due to any missing
        # ssh keys.
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        