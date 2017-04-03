#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections
import matplotlib.pyplot as plt
import re

str = re.sub(r'á',r'a',open('quijote.txt').read().lower())
str = re.sub(r'é',r'e',str)
str = re.sub(r'í',r'i',str)
str = re.sub(r'ó',r'o',str)
str = re.sub(r'ú',r'u',str)
str = re.sub(r'ñ',r'n',str)

words = re.findall(r'\w+',str)

c=collections.Counter(words)


prohibidas = re.findall(r'\w+', open('prohibidas.txt').read().lower())

for i in prohibidas:
	del c[i]
mc = c.most_common(5)
print mc

palabras =[]
cantidad = []

for i in mc:
	palabras.append(i[0])
	cantidad.append(i[1])

print palabras
print cantidad
	
xs	=	[i	+	0.1	for	i,	_	in	enumerate(palabras)]
plt.bar(xs,cantidad)

plt.ylabel("Cantidad de palabras")
plt.title("Palabras del Quijote")
plt.xticks([i	+	0.5	for	i,	_	in	enumerate(palabras)],	palabras)

plt.show()



