#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re


s = "\xa9"
if re.search(r'^[a-z]*[A-Z]*$', s):
	print s
