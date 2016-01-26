#!/usr/bin/env python
'''
Write a script using a telnet_device class that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
from time import sleep
import socket
import sys
import getpass

class telnet_device(object):
    def __init__(self,ip_addr,telnet_port,telnet_timeout):
        '''Establish telnet connection'''
        self.ip_addr=ip_addr
        self.telnet_port=telnet_port
        self.telnet_timeout=telnet_timeout
        try:
            self.conn=telnetlib.Telnet(ip_addr, telnet_port, telnet_timeout)
        except socket.timeout:
            self.conn=False
    def login(self,username,password):           
        '''Login to network device'''
        output = self.conn.read_until("sername:", self.telnet_timeout)
        self.conn.write(username + '\n')
        output += self.conn.read_until("ssword:", self.telnet_timeout)
        self.conn.write(password + '\n')
        sleep(1)
        output += self.conn.read_very_eager()
        return output
    def disable_paging(self, paging_cmd='terminal length 0'):
        '''Disable the paging of output (i.e. --More--)'''
        return self.send_command(paging_cmd)
    def send_command(self,cmd):
        '''Send a command down the telnet channel- Return the response'''
        cmd = cmd.rstrip()
        self.conn.write(cmd + '\n')
        sleep(1)
        return self.conn.read_very_eager()
    def close(self):
        '''Close the telnet connection'''
        self.conn.close()
        self.conn=False
        
def main():
    '''
    Script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr='50.76.53.27'
    telnet_port = 23
    telnet_timeout = 6
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()
    rtr1=telnet_device(ip_addr,telnet_port,telnet_timeout)
    if rtr1:
        output=rtr1.login(username,password)
        output=rtr1.disable_paging()
        output=rtr1.send_command('show ip int bri')
        print "\n\n"
        print output
        print "\n\n"
        rtr1.close()
if __name__ == "__main__":
    main()    
