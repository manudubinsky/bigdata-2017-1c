#!/usr/bin/python
# -*- coding: utf-8 -*-

import rethinkdb as r

r.connect("localhost",28015).repl()

cortos = []
medianos = []
largos = []

cursor = r.table("tweets").pluck("text").run()
for document in cursor:
	words = document["text"].split()
	if (len(words) < 10):
		cortos.append(document)
	elif ((len(words) > 10) and (len(words)< 20)):
		medianos.append(document)
	elif (len(words) > 20): 
		largos.append(document)
		
#Prueba cortos
for document in cortos:
	words = document["text"].split()
	print len(words)

print "---------------------"	

#Prueba medianos
for document in medianos:
	words = document["text"].split()
	print len(words)

print "---------------------"	

#Prueba largos
for document in largos:
	words = document["text"].split()
	print len(words)

print "---------------------"	

		
		
