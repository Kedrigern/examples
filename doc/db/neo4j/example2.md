CREATE (OpenCard:Project {id:'opencard', name:'OpenCard',description: 'Lorem ipsum...'})

CREATE (EMS:Firma {id:'ems', name:'E Money Service', legal:'s.r.o.'})
CREATE (OOC:Firma {nmae:'Operator OpenCard', legal:'a.s.'})

CREATE (Opatrny:Person {name:'Martin Opatrny', mob:''})
CREATE (Kostal:Person {name:'Ondřej Kostal', mob:'777583983'})
CREATE (Vychodil:Person {name:'Petr Vychodil', mob:''})

CREATE
	(EMS)-[:Realizuje {Role:'Puvodni dodavatel'}]->(OpenCard),
	(OOC)-[:Realizuje {Role:'Provozuje'}]->(OpenCard)

CREATE
	(Opatrny)-[:Pracuje {Role:'Obchodak'}]->(EMS),
	(Kostal)-[:Pracuje {Role:'Clen predstavenstva'}]->(OOC),
	(Vychodil)-[:Pracuje {Role:'Clen predstavenstva'}]->(OOC)

RETURN OpenCard
;

