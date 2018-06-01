#!/usr/bin/env python3

import urllib.request
import re

def get_external_ip():
    url = 'http://checkip.dyndns.org'
    requesty = urllib.request.urlopen(url).read()
    externalIP = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', requesty)
    return externalIP

print('Your public IP address is: ' + str(get_external_ip()) )