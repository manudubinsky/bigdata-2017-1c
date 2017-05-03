#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
a = 1
with open("paginas.txt",'r+') as file:
	#for line in file:
		file2 = open("archivo"+str(a)+".txt",'w')
	#	line = line.rstrip()
		html = requests.get("http://www.gov.uk").text
		#html = requests.get("http://www.bancogalicia.com/banca/online/web/Personas").text
		soup = BeautifulSoup(html, 'html5lib')

		for script in soup(["script", "style"]):
			script.extract()

		# print soup.text
		html_content = soup.prettify('latin-1')
		# html_content = soup.prettify().encode('utf-8')
		html_content = re.sub(r'<.*>', r'', html_content)
		for l in html_content.split('\n'):
			match = l.rstrip().strip().split()
			print match
			for x in match:
				if re.search(r'^([a-z]|[A-Z])*$', x):
					print x
					file2.write(x)
					file2.write(" ")
			file2.write("\n")
		# print html_content
		#	print soup.text
		a = a +1
