#!/usr/bin/env bash
# Author: Ondřej Profant
# http://www.openldap.org/faq/data/cache/104.html
# https://www.server-world.info/en/note?os=Fedora_24&p=openldap

echo "This is script for Fedora 24 and its only for dev purpose"

files="chrootpw.ldif chdomain.ldif basedomain.ldif"

for f in $files; do
	if [ -f "$f" ]; then :
	else 
		echo "No $f";
		exit 1;
	fi;
done;



function install() {
	echo "Install packages, create config, change user, start service"
	sudo dnf -y install openldap-servers openldap-clients
	cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
	chown ldap. /var/lib/ldap/DB_CONFIG
	systemctl start slapd
	sleep 2
}

function uninstall() {
	echo "Stoping LDAP, remove packages, remove configs"
	systemctl stop slapd
	sudo dnf -y remove openldap-servers openldap-clients
	rm -rf /var/lib/ldap
}

function configure() {
	echo "Heslo pro LDAP?"
	p1=`slappasswd`
	#p2=`slappasswd`
	sed -i "s/{SSHA}xxxxxxxxxxxxxxxxxxxxxxxx/${p1}/" chrootpw.ldif
	sed -i "s/{SSHA}xxxxxxxxxxxxxxxxxxxxxxxx/${p1}/" chdomain.ldif
	# replace to your own domain name for "dc=***,dc=***" section
	#sed -i "s///" basedomain.ldif

	# Set OpenLDAP admin password. 
	ldapadd -Y EXTERNAL -H ldapi:/// -f chrootpw.ldif 
	# Import basic Schemas.
	ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/cosine.ldif
	ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/nis.ldif
	ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/inetorgperson.ldif
	# Set your domain name on LDAP DB.
	ldapmodify -Y EXTERNAL -H ldapi:/// -f chdomain.ldif
	ldapadd -x -D cn=Manager,dc=srv,dc=world -W -f basedomain.ldif
}

function test() {
	echo "Querying database ..."
	ldapsearch -b 'dc=pirati,dc=cz' 'objectClass=*'
}

function full() {
	uninstall;
	install;
	test;
	configure;
	test;
}

full;
