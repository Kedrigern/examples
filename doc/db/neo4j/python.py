#!/usr/bin/env python3

import py2neo

user = 'neo4j'
passwd = 'lokomotiva23'
url = 'neo4j.pirati.cz'

def connect():
	# set up authentication parameters
	py2neo.authenticate(url, user, passwd)

	# connect to authenticated graph database
	return py2neo.Graph('http://' + url + '/db/data/')

def count_all(graph):
	return graph.cypher.execute('MATCH n RETURN count(n)')

g = connect()
c = count_all(g)
print(c)
