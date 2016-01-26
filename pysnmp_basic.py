#!/usr/bin/env python
'''
Write a script using a telnet_device class that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import pysnmp
from snmp_helper import snmp_get_oid, snmp_extract

class snmp_device(object):
    def __init__(self,ipaddr,commst,port):
        self.ipaddr=ipaddr
        self.commst=commst
        self.port=port
        self.device=(ipaddr,commst,port)
    def snmpquery(self,oid):
        return snmp_extract(snmp_get_oid(self.device,oid))
    def sysname(self):
        return self.snmpquery('1.3.6.1.2.1.1.5.0')
    def sysdesc(self):
        return self.snmpquery('1.3.6.1.2.1.1.1.0')

def main():
    community_string='galileo'
    ipaddr='50.76.53.27'
    rtr1=snmp_device(ipaddr,community_string,7961)
    rtr2=snmp_device(ipaddr,community_string,8061)
    print '\n\n',rtr1.sysname(),'\n', rtr1.sysdesc()
    print '\n\n',rtr2.sysname(), '\n',rtr2.sysdesc()

if __name__=="__main__":
    main()
    

