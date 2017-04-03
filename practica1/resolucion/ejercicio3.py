#!/usr/bin/python

import re

str = 'Hola.,.,.:;'

print re.sub(r'[\.\,\;\:]', r' ', str)
