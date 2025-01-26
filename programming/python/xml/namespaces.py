#!/usr/bin/env python3
# Parse xml with namespaces

from lxml import etree as ET

sample = """
<rdf:RDF xml:base="http://dbpedia.org/ontology/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns="http://dbpedia.org/ontology/">

    <owl:Class rdf:about="http://dbpedia.org/ontology/BasketballLeague">
        <rdfs:label xml:lang="en">basketball league</rdfs:label>
        <rdfs:comment xml:lang="en">
          a group of sports teams that compete against each other
          in Basketball
        </rdfs:comment>
    </owl:Class>

</rdf:RDF>
"""
fromFile = True

if fromFile:
  fp = 'ns.xml'
  tree = ET.parse(fp)
  root = tree.getroot()
else:
  root = ET.fromstring(sample)


namespaces = {'owl': 'http://www.w3.org/2002/07/owl#'}
ns1 = {'owl': 'http://www.w3.org/2002/07/owl#'}
ns2 = {'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'}

print("Root element: ", root)
print("owl:Class: ", root.findall('owl:Class', root.nsmap))
print('owl:Class/rdfs:label: ', root.findall('owl:Class/rdfs:label', root.nsmap))
print('owl:Class/rdfs:label text: ', root.findall('owl:Class/rdfs:label', root.nsmap)[0].text)