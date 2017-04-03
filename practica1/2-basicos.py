#!/usr/bin/python

import re

print re.search(r'iii', 'piiig').group()

print "******"

print re.search(r'..g', 'piiig').group()

print "******"

print re.search(r'\d\d\d', 'p123g').group()
print re.search(r'\w\w\w', '@@abcd!!').group()
