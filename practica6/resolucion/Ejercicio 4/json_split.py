#!/usr/bin/python

import json

tweets_data_path = 'elecciones.txt'

tweets_file = open(tweets_data_path, "r")
a = 0
x = 1
c = 354350
outfile = open('prueba'+str(x)+'.txt', 'w')
for line in tweets_file:
	a = a + 1
	try:
		tweet = json.loads(line)
		json.dump(tweet, outfile)
		if (a > c/10):
			a = 0
			x = x + 1
			outfile.close()
			outfile = open('prueba'+str(x)+'.txt', 'w')
	except:
		continue

	
		
