#!/usr/env/bin python3
#Usage: python .\IPparser.py .\fileTOparse
#searches for all IPv4 addresses

import re, sys
from collections import Counter

print('	IPv4 Addresses in the Logs ')
print('=' * 50)
def log_reader(logfile):
    rex = r'([^-/\D]\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^-/])'

    with open(logfile) as file:
        log = file.read()
        ip_list = re.findall(rex,log)
        ipcount = Counter(ip_list)
        for a, b in ipcount.items():
            print( "Count = " + str(b) + "	   " + str(a))


if __name__ == '__main__':
    log_reader(sys.argv[1])
	

print('=' * 50)
