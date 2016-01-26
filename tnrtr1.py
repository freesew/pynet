#!/usr/bin/env python
from pprint import pprint
import telnetlib
from time import sleep
ip_addr='50.76.53.27'
telnet_port=23
telnet_timeout=6
remote_conn=telnetlib.Telnet(ip_addr,telnet_port,telnet_timeout)
output=remote_conn.read_until('sername',telnet_timeout)
print(output)
remote_conn.write('pyclass'+'\n')
output=remote_conn.read_until('assword:',telnet_timeout)
print(output)
remote_conn.write('88newclass'+'\n')
sleep(1)
output=remote_conn.read_very_eager()
print(output)
remote_conn.write('terminal length 0'+'\n')
sleep(1)
output=remote_conn.read_very_eager()
print(output)
remote_conn.write('sho ip int bri'+'\n')
sleep(1)
output=remote_conn.read_very_eager()
print(output)
remote_conn.close()

