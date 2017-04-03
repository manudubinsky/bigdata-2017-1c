#!/usr/bin/python

import re


str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
	print email

print "********"

#findall y tuplas
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples
for tuple in tuples:
	print tuple[0]
	print tuple[1]
