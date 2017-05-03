import collections
import re


lista=[]
lista2=[]

with open("top-1m.csv",'r+') as file:
	for line in file:
		text = re.findall(r'\.\w{2}$', line)
		if text:
			lista.append(text[0])

for x in lista:
		x = re.sub(r'(\.)(\w{2})',r'\2',x)
		lista2.append(x)
		
#print lista2[0]
c=collections.Counter(lista2)

#mc = c.most_common(5)
#print mc

c = dict(c)
with open("paises.csv","r+") as file:
	for line in file:
		 match = line.rstrip().split(',')
		 if match[1] in c :
			print match[0]+","+str(c[match[1]])
         


	
