#!/usr/bin/env python3

import csv
import json
from pprint import pprint
from urllib.request import urlopen

__author__ = "Ondřej Profant"
__doc__ = """
Generates list of members of Czech Pirate Party from graph.pirati.cz

Welcome to Graph API for pirati.cz. This website provides access to social graph.

Every object in the social graph has a unique ID. You can access the properties of an object by requesting http://graph.pirati.cz/ID

To list users use http://graph.pirati.cz/users

To list groups use http://graph.pirati.cz/groups

You can search for users and/or groups by using these urls:

    http://graph.pirati.cz/user/USERNAME
    http://graph.pirati.cz/group/USERNAME

User-group relations can be gathered like this:

    http://graph.pirati.cz/user/USERNAME/groups
    http://graph.pirati.cz/ID/groups
    http://graph.pirati.cz/group/USERNAME/members
    http://graph.pirati.cz/ID/members
"""


dot = "%2E"
space = "%20"

group = "Celostatni%20forum"
url = "https://graph.pirati.cz/group/{group}/members".format(group=group)

def get_json(url):
    raw_data = urlopen(url).read().decode('utf8')
    return json.loads(raw_data)

def get_cf():
    group = "Celostatni%20forum"
    url = "https://graph.pirati.cz/group/{group}/members".format(group=group)
    return get_json(url)

def get_user(username):
    url = "https://graph.pirati.cz/user/{username}".format(username=username)
    return get_json(url)

def get_members_data():
    members_nick = [m['username'] for m in get_cf()]
    print("Members count: {0}".format(len(members_nick)))
    members = []
    for m in members_nick:
        print(".", end="", flush=True)
        members.append(get_user(m))
    print("|")
    return members

def csv_write(data, filename="members.csv"):
    with open(filename, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # header
        writer.writerow(["name", "surname", "email", "username", "address", "rank"])
        for d in data:
            if d['fullname']:
                fullname = d['fullname'].rsplit(" ", 1)
            else:
                fullname = d['username'].rsplit(".", 1)
            record = fullname + [d["email"], d["username"], d["address"], d['rank']]
            writer.writerow(record)

def from_usernames_create_csv(usernames, filename="members.csv"):
    with open(filename, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["username", "email", "name"])
        for u in usernames:
            writer.writerow([u, u + "@pirati.cz", u.replace(".", " ")])

csv_write(get_members_data())
