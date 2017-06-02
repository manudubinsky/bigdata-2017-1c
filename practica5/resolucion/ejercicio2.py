#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from time import sleep
#import psycopg2

#CADA VEZ QUE SE EJECUTE POR PRUEBAS TRUNCAR LAS TABLAS

prov = ["Buenos Aires","Santa Fe","Cordoba","Entre Rios",
"Tierra del Fuego","La Pampa","Misiones","Chaco","Tucuman",
"Jujuy","Rio Negro","Chubut","Santa Cruz","Mendoza","Catamarca",
"Santiago del Estero","Salta","Corrientes","Neuquen","San Juan",
"La Rioja", "Formosa","San Luis"]

def cleanCategoriaAutor(nombrecol,p):
	#la idea es "limpiar" de caracteres que te puedan traer problemas y completar desde aca
	#las tablas Categoria y Autor
	listnom=[]
	for x in p:
		categoria = p.find('span').text
		catnomautmail= re.sub(r'\n',r'',categoria)
		catnomautmail= re.sub(r'[^\x00-\x7f]',r'',catnomautmail)
		catnomautmail= re.sub(r'(\s)+',r' ',catnomautmail)
		listnom.append(catnomautmail)
		
	#QUITO DUPLICADOS
	listnom=list(set(listnom))
	insertCategoriaAutor(nombrecol,listnom)
	
def insertCategoriaAutor(col,listnom):
	
	conn = psycopg2.connect(dbname='prueba',user='postgres',host='localhost',password='undav')
	cursor = conn.cursor()
	for x in listnom:
		query =  "INSERT INTO categoria ("+	col +") VALUES ("+ "'"+ x +"'"+");"
		data = (str(x))
		cursor.execute(query)
		conn.commit()
		
def articulos(table):
	td = table.find('td', width = "425")
	p = td.find('p')
	categoria = p.find('span').text
	#cleanCategoriaAutor("nombre",p)
	for tr in table('tr'):
		if tr.find('td', width = "36"):
			td1 = tr.find('td', width = "36")
			p1 = td1.find('p')
			idArticulo = p1.find('span').text
		if tr.find('td', width = "108"):	
			td2 = tr.find('td', width = "108")
			p2 = td2.find('p')
			titulo = p2.find('span').text
		if tr.find('td', width = "281"):
			td3 = tr.find('td', width = "281")
			p3 = td3.find('p')
			for span in p3('span'):
				if(re.search(r'[\w.-]+@[\w.-]+', span.text)):
					match = re.search(r'[\w.-]+@[\w.-]+', span.text)
					autor = match.group()
					#insertArticulo(categoria,idArticulo, titulo, autor) #aca no tendria que tomar todo el texto sino la parte de categoria que le corresponda
		            
		      
#ACA NO QUISIERA RESCATAR EL NOMBRE SINO EL MAIL PARA PARTIR ESTE ITEM COMO HICE CON CATEGORIA
#Y LLENAR ESA TABLA APARTE
#NO LO TOQUE PORQUE TODAVIA NO ENTIENDO BIEN COMO FUNCIONA		      
def insertArticulo(categoria,idarticulo, titulo, autor):
	
	conn = psycopg2.connect(dbname='prueba',user='postgres',host='localhost',password='undav')
	cursor = conn.cursor()
	#PRIMERO TOMARIA EL ID DEL AUTOR (idem tomar id de categoria)
	#DESPUES TOMARIA EL ID DE LA CATEGORIA
	
	query =  "SELECT * FROM categoria WHERE nombre =" + "'"+categoria+"'"+";"
	cursor.execute(query)
	idcategoria=cursor.fetchall()
	conn.commit()
	#PRUEBA
	for x in idcategoria:
		print x

def universidades(table,lista):
	for tr in table('tr'):
		if(tr.find('td',width = "281")):
			td = tr.find('td', width = "281")
			p = td.find('p')
			for span in p('span'):
				if (re.search(r'([\w.-]+)@([\w.-]+.edu.ar)', span.text)): 
					match = re.search(r'([\w.-]+)@([\w.-]+.edu.ar)', span.text)
					lista.append(match.group(2))

lista = []
html = open("articulosAceptadosFrame.html")
soup = BeautifulSoup(html.read(), 'html5lib')

for table in soup('table'):
	articulos(table.find('tbody'))
	universidades(table.find('tbody'),lista)
lista = list(set(lista))

for l in lista:
	html = requests.get("http://"+l).text
	soup = BeautifulSoup(html, 'html5lib')
	#for a in prov:
	#	if(re.search(a,string)):
	#		provinicia = re.search(a,string) #No se si esto se hace asi
	#		print provincia
	nombre = soup.find('title').text
	print nombre
	   
