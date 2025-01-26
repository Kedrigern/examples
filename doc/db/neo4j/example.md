

CREATE (MHMP:Instituce {label: 'Magistrát', name: 'Magistrát Hl. m. Prahy', address:''})
CREATE (RHMP:Instituce {label: 'Rada', name:'Rada Hl. m. Prahy', address:''})
CREATE (ZHMP:Instituce {label: 'Zastupitelstvo', name: 'Zastupitelstvo Hl. m. Prahy', address:''})

CREATE (pirati:Strana {label: 'Pirati', name:'Česká pirátská strana'})
CREATE (CSSD:Strana {label: 'ČSSD', name:'Česká strana sociálně demokratická'})
CREATE (trojkoalice:Strana {label: '3K', name:'Trojkoalice'})
CREATE (top:Strana {label: 'TOP09', name:'Top09'})
CREATE (kdu:Strana {label: 'KDU', name:'Kdu-Čsl'})
CREATE (nezavisli:Strana {label: 'Nez', name:'Nezavislí'})
CREATE (zeleni:Strana {label: 'Zelení', name: 'Strana Zelených', description:''})

CREATE (profant:Person {name: 'Ondřej Profant', description:''})
CREATE (michalek:Person {name: 'Jakub Michálek', description:''})
CREATE (ferjencik:Person {name: 'Mikuláš Ferjenčík', description:''})
CREATE (zabransky:Person {name: 'Adam Zábranský', description:''})
CREATE (mirovsky:Person {name: 'Ondřej Mirovský', description:''})
CREATE (stropnicky:Person {name: 'Matěj Stropnický', description:''})
CREATE (cizinsky:Person {name: 'Jan Čižinský', description:''})
CREATE (hudecek:Person {name: 'Tomáš Hudeček', description:''})
CREATE (dolinek:Person {name: 'Petr Dolinek', description:''})


CREATE
	(profant)-[:Clen]->(ZHMP),
	(profant)-[:Clen]->(pirati),
	(michalek)-[:Clen]->(ZHMP),
	(michalek)-[:Clen]->(pirati),
	(ferjencik)-[:Clen]->(ZHMP),
	(ferjencik)-[:Clen]->(pirati),
	(zabransky)-[:Clen]->(ZHMP),
	(zabransky)-[:Clen]->(pirati),
	(mirovsky)-[:Clen]->(ZHMP),
	(mirovsky)-[:Clen]->(trojkoalice),
	(mirovsky)-[:Clen]->(zeleni),
	(stropnicky)-[:Clen]->(trojkoalice),
	(stropnicky)-[:Clen]->(ZHMP),
	(stropnicky)-[:Clen]->(zeleni),
	(cizinsky)-[:Clen]->(ZHMP),
	(cizinsky)-[:Clen]->(trojkoalice),
	(cizinsky)-[:Clen]->(kdu),
	(hudecek)-[:Clen]->(ZHMP),
	(hudecek)-[:Clen]->(RHMP),
	(hudecek)-[:Clen]->(nezavisli),
	(dolinek)-[:Clen]->(ZHMP),
	(dolinek)-[:Clen]->(CSSD)

CREATE
	(ZHMP)-[:Ridi]->(RHMP),
	(RHMP)-[:Ridi]->(MHMP)

RETURN MHMP, RHMP, ZHMP
