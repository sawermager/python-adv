#!/usr/bin/env python

"""
Brief: Demonstrate using SSH via paramiko to get information from
the network and print to screen.
"""

import time
import paramiko

R1="10.215.187.82"
R2="10.215.187.74"


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
    
def get_output(conn):
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
        R1: "ip addr",
        R2: "ip addr",
    }

    # For each host in the inventory dict, extract key and value
    for hostname, vrf_cmd in host_dict.items():
        
        # paramiko can be ssh client or server; use client here
        conn_params = paramiko.SSHClient()
        
        # We don't need paramiko to refuse connections due to any missing
        # ssh keys.
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn_params.load_system_host_keys()
        conn_params.connect(
            hostname=hostname,
            port=22,
            username="sawermager",
            password="password",
        ) 

        # Get an interactive shell and wait a bit for the prompt to appear
        conn = conn_params.invoke_shell()
        time.sleep(1.0)

        # This is a way to capture the prompt and output
        print(f"Logged into {get_output(conn).strip() } successfully")
        
        # Iterate over the list of command, sending each one in series
        # The final command in the list is the OS-specific VRF "show" command
        commands = [

            # Set terminal length to unlim to avoid the 'more' pagination that
            # happens with many cli's
            #"terminal length 0",
            #"show version | include Software,",
            "cat /etc/lsb-release",
            vrf_cmd,
        ]
        concat_output = ""
        for command in commands:
            
            # It helps to give a custom funtion to abstract sending
            # commands and reading output from the device
            send_cmd(conn, command)
            #breakpoint() (new to python 3.7)
            concat_output += get_output(conn)

        # Close the session when we are done
        conn.close()

        # Open file per host and write output
        print(f"Writing {hostname} output to file")
        with open(f"{hostname}_output.txt", "w") as handle:
            handle.write(concat_output)

if __name__ == "__main__":
    main()
