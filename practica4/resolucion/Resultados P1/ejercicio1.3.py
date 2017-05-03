import collections
import re

d={}
lista=[]
lista2=[]
relevancia=20000000
with open("top-1m.csv",'r+') as file:
	for line in file:
		text = re.findall(r'\.\w{2}$', line)
		if text:
			lineaux=re.sub(r'(\.)(\w{2})',r'\2',text[0])
			if lineaux:
				if lineaux in d :
					d[lineaux]= d[lineaux] + relevancia 
				else:
					d[lineaux]= relevancia 
		relevancia=relevancia-10

with open("paises.csv","r+") as file:
	for line in file:
		 match = line.rstrip().split(',')
		 if match[1] in d :
			print match[0]+","+str(d[match[1]])
