import collections
import re

d={}
lista=[]
lista2=[]
relevancia=200000000

with open("top-1m.csv",'r+') as file:
        for line in file:
                text = re.findall(r'(edu\.\w{2})$', line)
                if text:
                        lineaux=re.sub(r'(\w{3})(\.)(\w{2})',r'\3',text[0])
                        if lineaux:
                                if lineaux in d:
                                        d[lineaux] = d[lineaux] + relevancia 
                                else:
                                        d[lineaux] = relevancia 
                relevancia = relevancia-10

# ar br uy py cl bo
# se pueden restringir aca o desde choroplethr
with open("paises.csv","r+") as file:
        for line in file:
                 match = line.rstrip().split(',')
                 if match[1] in d :
                        print match[0]+","+str(d[match[1]])

