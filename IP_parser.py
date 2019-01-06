#!/usr/env/bin python3
#Usage: PS C:\>python .\IPparser.py .\fileTOparse
#searches for all IPv4 addresses

import re
from collections import Counter
import sys

print('		IP Addresses in the Logs')
print('		========================')
def log_reader(logfile):
    rex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    with open(logfile) as file:
        log = file.read()
        ip_list = re.findall(rex,log)
        ipcount = Counter(ip_list)
        for a, b in ipcount.items():
            print("IPv4" + "== " + str(a) + "	" + "Count "  + "== " + str(b))


if __name__ == '__main__':
    log_reader(sys.argv[1])
	

print('		=========================')
