#!/usr/env/bin python3
#Usage: PS C:\>python .\URLparser.py .\fileToparse
#searches for all URLs

import re
from collections import Counter
import sys

print('			URLs in the Logs    	')
print('		========================')
def log_reader(logfile):
    rex = r'([a-z][:\-\.\w\/]+?\.([a-z]+?)(:*\d*)/\S)'

    with open(logfile) as file:
        log = file.read()
        url_list = re.findall(rex,log)
        urlcount = Counter(url_list)
        for a, b in urlcount.items():
            print("Domain " + "== " + str(a) + "	" + "Count "  + "== " + str(b))

			
if __name__ == '__main__':
    log_reader(sys.argv[1])
	
print('		========================')
