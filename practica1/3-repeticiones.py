#!/usr/bin/python

import re

print re.search(r'pi+', 'piiig').group()

print "******"

print re.search(r'i+', 'piigiiii').group()

print "******"

print re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx').group()
print re.search(r'\d\s*\d\s*\d', 'xx12  3xx').group()
print re.search(r'\d\s*\d\s*\d', 'xx123xx').group()

print "******"

print re.search(r'b\w+', 'foobar').group()
print re.search(r'^b\w+', 'foobar')
