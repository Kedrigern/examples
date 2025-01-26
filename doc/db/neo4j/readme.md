Neo4j
=====

[Neo4j](http://neo4j.com) je grafová databáze s velmi příjemným uživatelským rozhraním.

Pokud ji máme nainstalovanou, tak naslouchá na portu `7474`, popřípadě má velmi hezké webové rozhraní: `http://localhost:7474/browser/`, resp `/webadmin/`


Grafové databáze
----------------

### Ontologie

Je schéma dle kterého je graf sestavován. V `neo4j` je struktura volná.


Instalace a spuštění
--------------------

### Debian

Repozitář: `http://debian.neo4j.org/`

```
apt-get update
apt-get install neo4j
```

Obsluhuje se jako jakýkoliv jiný démon:

```service neo4j start```

popřípadě subpříkazy `stop` a `restart`.

### Fedora 21 a 22

`http://yum.neo4j.org/`


### Docker

```
docker pull tpires/neo4j:latest
docker run -d --name neo4j --cap-add=SYS_RESOURCE -p 7474:7474 tpires/neo4j
```

Bohužel tento obraz založený na Debianu obsahuje velmi starou verzi 2.1.*.

Existuje i oficiální obraz: `docker pull neo4j/neo4j`

Příkazy
-------

Základní klíčová slova jsou: `MATCH`, `WHERE`, `RETURN`, `CREATE`, `MERGE`, `DELETE`, `SET`, `FOREACH`, `WITH`, `LOAD CSV`, `UNWIND`, `START`, `CREATE UNIQUE`.
Použití vypadá např. takto: ```MATCH <pattern> WHERE <conditions> RETURN <expressions>```

V interaktivní příkazovém řádku můžeme zadat: `:help COMMAND` a dostaneme nápovědu.


### Vytvoření uzlu
```
CREATE (jd:Person { name: "Joe", surname: "Doe", from: "Sweden", age: 27 })
```

`()` závorky značí uzel, `jd` je název proměnné (uzlu), `Person` je popis, `{key: "val", ...}` jsou vlastnosti uzlu.


Popřípadě lze i více entit najednou:

```
CREATE (jd:Person { name: "Joe", surname: "Doe", age: 27 }),
(jb:Person { name: "Joe", surname: "Brown", age: 28}),
(ab:Person { name: "Anne", surname: "Brown", age: 26}),
(jb)-[:KNOWS]->(ab)
```


Smazání uzlů i vztahů:
```MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r```


Nástroje
--------

### Py2Neo

Install: `pip install py2neo`


```python
from py2neo import Graph, Path
graph = Graph()

tx = graph.cypher.begin()
for name in ["Alice", "Bob", "Carol"]:
    tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
alice, bob, carol = [result.one for result in tx.commit()]

friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
graph.create(friends)
```



Links
-----

### Obecné

* [neo4j.cz](neo4j.cz)
* [seriál Zdroják](http://www.zdrojak.cz/clanky/grafova-terminologie-a-dostupne-technologie/)
* [dokumentace](http://docs.spring.io/spring-data/neo4j/docs/current/reference/html/)
* [dokumentace rozcestník](http://neo4j.com/docs/milestone/)
* [blog](http://jexp.de/blog/2013/04/cool-first-neo4j-2-0-milestone-now-with-labels-and-real-indexes/)

### Konkrétní

* [Identity and Access Management](http://gist.neo4j.org/?4471127413fd724ed0a3)
* [Resources](http://gist.neo4j.org/?8141937)
[](http://gist.neo4j.org/?8141937)
