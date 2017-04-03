#!/usr/bin/python

import re

str = 'Xan examplXe word:cat!! aiosdi IVaslkdj XI'
match = re.search(r'\s+[XVLMCDI]+\s+|\s+[XVLMCDI]+$|^[XVLMCDI]+\s+', str)
if match:                      
	print 'found', match.group() 
else:
	print 'did not find'
