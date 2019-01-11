#!/usr/env/bin python3
#Usage: python .\URLparser.py .\fileToparse
#searches for all URLs

import re, sys
from collections import Counter


print('			URLs in the Logs	')
print('=' * 50)
def log_reader(logfile):
    rex = r'([a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,9}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*)'

    with open(logfile) as file:
        log = file.read()
        url_list = re.findall(rex,log)
        urlcount = Counter(url_list)
        for a, b in urlcount.items():
            print( "Count = " + str(b) + "	   " + str(a))

			
if __name__ == '__main__':
    log_reader(sys.argv[1])
	
print('=' * 50)
