#!/usr/bin/python

import re


str = 'Mariano,Vecco,12435657/Victoria,Caparelli,345436346'

tuples = re.findall(r'(\w+),(\w+)', str)

print tuples
for tuple in tuples:
	print tuple[1]+" "+tuple[0]
