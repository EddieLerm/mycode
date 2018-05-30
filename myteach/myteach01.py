#!/usr/bin/env python3

import ipaddress

myipaddress ='192.168.0.1'

ipv = ipaddress.ip_address(myipaddress)

print(dir(ipv))

if (ipv.is_private()): 
    print("Its private")