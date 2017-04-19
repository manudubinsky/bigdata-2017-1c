import re

import csv
pais=""
text=re.sub(r'"(\d+)(,\d+)"',r'\1',open("LeeLee_enroll_MF.csv").read().lower())#redondeo (mejorar)
#text2=re.sub(r'([a-z])(,)(\s*[a-z]+)',r'\1 \3',text) #paises que tienen coma, hay que cambiar la expresion regular para casos donde el separador sea la ,
matchme=text.splitlines()


with open("LeeLee_enroll_MF.csv",'wb') as file:
    for line in matchme:
                  match = line.split(',')#cuando el separador es la coma hay que usar ','
                  if(len(match[0])!=0):
                      pais= match[0]
                      
                  line=pais+','+','.join(match[1:7])
                  
                  if(re.match(r'^\w+,\w+',line)):
                      print line
                      file.write(line+'\n')
file.close()
          


#australia,1820,"21,6",0,0,"advanced economies"
#australia,1825,"23,79",0,0,"advanced economies"
#australia,1830,"26,13",0,0,"advanced economies"
#australia,1835,"28,61",0,0,"advanced economies"
#australia,1840,"31,23",0,0,"advanced economies"
#australia,1845,"33,98",0,0,"advanced economies"
