echo "Run with sudo (Fedora)"

echo "Download images"
docker pull mariadb:10.1
docker pull osixia/openldap:1.1.6
docker pull sameersbn/redmine:3.3.0-4

echo "Create docker internal network"
docker network create docker-ldap

echo "Run LDAP at port 3890"
docker run -d --name ldap --env LDAP_ORGANISATION="Piratska strana" --env LDAP_DOMAIN="pirati.cz" --env LDAP_ADMIN_PASSWORD="admin" --volume ldap-data:/var/lib/ldap:Z --volume ldap-config:/etc/ldap/slapd.d:Z -p 3890:389 --net docker-ldap --net-alias ldap osixia/openldap:1.1.6

echo "Run MariaDB for redmine"
docker run -d --name redmine-mariadb -v redmine-mariadb:/var/lib/mysql:Z --net docker-ldap --net-alias mariadb \
 -e MYSQL_ROOT_PASSWORD=pw -e MYSQL_DATABASE=redmine -e MYSQL_USER=redmine -e MYSQL_PASSWORD=redmine \
 mariadb:10.1

ip=`sudo docker network inspect docker-ldap | grep -A 4 redmine-mariadb | grep IPv4 | cut -d '"' -f 4 | cut -d "/" -f 1`
rm_port=8181

echo "Run Redmine at port $rm_port"
docker run -d --name redmine -p "${rm_port}:80" -v redmine-data:/home/redmine/data:Z --net docker-ldap --net-alias redmine \
 -e 'DB_TYPE=mysql' --env="DB_HOST=${ip}" -e 'DB_NAME=redmine' -e 'DB_USER=redmine' --env='DB_PASS=redmine' \
 sameersbn/redmine:3.3.0-4

echo "Configure LDAP by http://www.redmine.org/projects/redmine/wiki/RedmineLDAP"
