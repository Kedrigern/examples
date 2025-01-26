
# Ldap

Jedná se sice o prastarý a nepřiliš přívětivý protokol, avšak nejvíce rozšířenou autentifikační vrstvu.

LDAP je *lightweight protocol for accessing directory servers*. *Directory server* je *hierarchical object orientated database*.

V praxi to znamená, že správce si určuje komplexní DB schéma víceméně pomocí **objektů**. Lightweight protože je jednoduší než X.500 protokol. Je optimalizovaný pro čtení (proto strom). Je case insensitive.

Objekty v LDAPu obsahují **atributy**. Ty jsou množiny párů klíč-hodnota. Protože jsou data v rámci LDAP strukturovaná, tak objekty mohou obsahovat pouze validní klíče. Validita je zavislá na typu objektu (na schématu). Třídy mohou mít atributy povinné (mandatory) a volitelné (optional). Atribut může být single nebo multi. Multi dovoluje více hodnot (např. více emailových adres u jedné osoby). Atributy mohou mít aliasy nebo zkratky (cn je zkratka pro CommonName).

Matoucí je, že objekty mohou být více jak jednou třídou. Třídy:

- **strukturální** (structural): každý objekt má právě jednu. Jsou určeny k mapování fyzického obejktu, např. osoby či sítě. Tato třída nemůže být u obejtku změněna.
- **pomocné třídy** (auxilary): určují další typy atributů. Mohou být měněny u již existujícícho objektu.
- **abstraktní třídy** (abstract): nepřiřazují se přímo k obejtku, ale využívají je ostatní třídy v rámci hiearchie.

## Slovník

| Zkratka | Význam             | Příklad                                     | Vysvětlení                                               |
|---------|--------------------|---------------------------------------------|----------------------------------------------------------|
| DN      | Distinguished Name | DC=cz,DC=pirati,OU=people,cn=ondrej.profant | jednoznačné určení v rámci stormu (hiearchie)            |
| RDN     | Relative Distinguished Name | rdn = cn = ondrej.profant          | relativn9 jednoznačné označení (např. mezi usery) |
| DC      | Domain component   | google; com; cz; pirati                     | lze používat i geografické specifikace, ale DNS je lepší |
| OU      | Organization unit  | people; groups                              |  |
| CN      | Common name        |                                             |  |
| OID     | Object ID          | 1.3.6.1.4.1.1466.115.121.1.15{16}           | 16-character sized Unicode string |
| UID     | Unique ID          | ISBN; ID; URI                               | jednoznačný identifikator |
| DIT     | Directory Information tree |                                     | |
| LDAP    | Lightweight directory protocol |                                 | LDAP |
| LDIF    | LDAP Data interchange files | <filename>.ldif                    | Soubor s konfigurací pro LDAP |

### Grafická správa

- [Luma][] LDAP browser napsaný v Pythonu (PyQt).
- [Apache directory studio][] robustní řešení postavené nad Eclipse

## Schéma

Strom (není schéma):
```
                       DC = CZ
                          |
                      DC = Pirati
       	__________________|__________________________________________
       /                  |                       \                  \
OU = users          OU = systems            OU = organization    cn = admin
|-CN=John Doe      /      |    \                   |      
|-...       CN=Redmine CN=Forum CN=Wiki         OU = CF  
                                     ______________|_________________
                                    /             |           |      \                                
                                  OU=Praha   OU=Jihomoravsky  OU=Zlin   ...
```

Základní používaná schémata (předpřipravené množiny tříd):
```
include /etc/openldap/schema/core.schema
include /etc/openldap/schema/cosine.schema
include /etc/openldap/schema/inteorgperson.schema
include /etc/openldap/schema/misc.schema
include /etc/openldap/schema/nis.schema
```


## Docker      

`osixia/openldap:1.1.6 `

```
sudo docker run --env LDAP_ORGANISATION="Piratska strana" --env LDAP_DOMAIN="pirati.cz" --env LDAP_ADMIN_PASSWORD="admin" --volume data:/var/lib/ldap:Z --volume config:/etc/ldap/slapd.d:Z -p 3890:389 osixia/openldap:1.1.6
```

```
sudo docker exec ldap ldapsearch -x -h localhost -b dc=pirati,dc=cz -D "cn=admin,dc=pirati,dc=cz" -w <passwd>
```

## Fedora 24

### Install

```bash
dnf -y install openldap-servers openldap-clients
cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
chown ldap. /var/lib/ldap/DB_CONFIG
systemctl start slapd
systemctl enable slapd
```

### Configure F24

| Cesta                              | Význam                                            |
|------------------------------------|---------------------------------------------------|
| `/etc/openldap/`                   | adresář s konfigurací                             |
| `/etc/openldap/ldap.conf`          | konfigurace v rámci systému, např. default search |
| `/etc/openldap/slapd.ldif`         | hlavní LDIF soubor importuje `schema/core.ldif`   |
| `/etc/openldap/schema/`            | adresář se základními objekty                     |
| `/etc/openldap/schema/core.ldif`   |                  |
| `/var/lib/ldap/*`                  | data                                              |
| `/usr/share/openldap-servers/`     | example configy                                   |
| `/usr/share/doc/openldap-servers/guide.html` | velmi podrobný návod                |

```bash
# generate encrypted password into cli
slappasswd
```

[ldap-basics]: http://www.davidpashley.com/articles/ldap-basics/
[ldap-a-gentle-introduction]: https://hynek.me/articles/ldap-a-gentle-introduction/
[what-are-cn-ou-dc-in-an-ldap-search]: http://stackoverflow.com/questions/18756688/what-are-cn-ou-dc-in-an-ldap-search
[ldap]: http://www.zytrax.com/books/ldap/ch2/
[fedora24]: https://www.server-world.info/en/note?os=Fedora_24&p=openldap
[Luma]: http://luma.sourceforge.net
[Apache directory studio]: http://directory.apache.org/studio/
[osixia]: https://hub.docker.com/r/osixia/openldap/
