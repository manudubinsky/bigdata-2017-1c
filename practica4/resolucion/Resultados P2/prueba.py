#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

html = requests.get("http://www.gov.uk").text
#html = requests.get("http://www.bancogalicia.com/banca/online/web/Personas").text
soup = BeautifulSoup(html, 'html5lib')

for script in soup(["script", "style"]):
	script.extract()

html_content = soup.text
html_content = re.sub(r'<.*>', r'', html_content)
for l in html_content.split('\n'):
	match = l.rstrip().strip().split()
	print match
	for x in match:
		if re.search(r'^([a-z]|[A-Z])*$', x):
			print x
