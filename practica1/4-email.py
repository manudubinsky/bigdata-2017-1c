#!/usr/bin/python

import re

#1er intento...
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
	print match.group()

print "******"

#corchetes
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
	print match.group()

print "******"

#parentesis
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
	print match.group()
	print match.group(1)
	print match.group(2)
