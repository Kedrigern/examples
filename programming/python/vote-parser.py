#!/usr/bin/env python3

__version__ = "v1.0.0"
__author__ = "Ondřej Profant"
__description__ = """
Parse html file which are produced by voting information system of Prague city hall.
"""

import os
import sys
import json
import pprint
import argparse
from lxml import html


class VotingResult:
	"""
	Holds result of one one.

	 Structure:
	 - title (cs: hlasování)
	 - session (cs: zasedání)
	 - result (cs: výsledek)
	 - ...
	"""
	def __init__(self):
		self.session = None
		self.title = None
		self.result = None
		self.attendance = None
		self.votes = {'vote_for': None, 'vote_agains': None, 'abstain': None}
		self.parties = []

	def print_cmd(self):
		print(self.title, "/", self.session)
		print(self.attendance)
		print(self.result)
		print(self.parties)

	def print_xml(self):
		print('<voting>')
		print('\t<title>%s</title>' % self.title)
		print('\t<result>%s</result>' % self.result)
		print('\t<session>%s</session>' % self.session)
		print('</voting>')

	def print_json(self):
		json.dump(self.__dict__, sys.stdout, sort_keys=True, skipkeys=True, indent=2, ensure_ascii=False)

	def print_csv(self, out_file):
		pass


class Parser:

	def __init__(self):
		self.tree = None

	def parse_file(self, filename):
		self.tree = html.parse(filename)
		vr = VotingResult()
		self._parse_meta(vr)
		self._parse_results(vr)
		return vr

	def parse_files(self, filenames):
		results = []
		for f in filenames:
			results.append(self.parse_file(f))
		return results

	def _parse_meta(self, votingResult):
		votingResult.session = self.tree.xpath("/html/body/center/table/tr[1]/td[2]/p[@class='title']/text()")[0]
		votingResult.title = self.tree.xpath("/html/body/center/table/tr[1]/td[2]/p[2]/text()")[0].strip('\r')
		votingResult.result = self.tree.xpath("/html/body/center/center/table/tr[1]/td[1]/b/text()")[0]
		votingResult.attendance = self.tree.xpath("/html/body/center/center/table/tr[1]/td[1]/table/tr[1]/td[1]/text()")[0]
		votingResult.votes['vote_for'] = self.tree.xpath("/html/body/center/center/table/tr[1]/td[1]/table/tr[1]/td[2]/text()")[0]
		votingResult.votes['vote_agains'] = self.tree.xpath("/html/body/center/center/table/tr[1]/td[1]/table/tr[1]/td[3]/text()")[0]
		votingResult.votes['abstain'] = self.tree.xpath("/html/body/center/center/table/tr[1]/td[1]/table/tr[1]/td[4]/text()")[0]

	def _parse_results(self, votingResult):
		all_party = self.tree.xpath("/html/body/center[2]/table")

		for party_node in all_party:
			party = {}
			party['name'] = party_node.find('./tr[1]/td[1]/table/tr/th[1]').text
			party['result'] = party_node.find('./tr[1]/td[1]/table/tr/th[2]').text.rstrip(') ').lstrip('( ')

			members = party_node.xpath('./tr[2]/td/table/tr/td[@class="votename"][not(contains(text(),"\xa0"))]/text()')
			members = list(map(lambda x: x.rstrip(":"), members))
			votes = party_node.xpath('./tr[2]/td/table/tr/td[@class="votechoice"]/text()')

			party['results'] = list(zip(members, votes))
			votingResult.parties.append(party)

def main():
	p = argparse.ArgumentParser(
		description=__doc__,
		epilog="Version: " + __version__ + ", Authors: " + str(__author__)
		)
	p.add_argument('-f', '--format', default="resume", help="Options: resume, json, xml, csv")
	p.add_argument('-o', '--output', help="")
	p.add_argument('inputs', metavar='input files', nargs='*', help='Input files')
	args = p.parse_args()
	parser = Parser()
	vrs = parser.parse_files(args.inputs)

	if args.format == "resume":
		for vr in vrs:
			vr.print_cmd()
	elif args.format == "csv":
		raise NotImplementedError
	elif args.format == "json":
		for vr in vrs:
			vr.print_json()
	elif args.format == "csv":
		raise NotImplementedError
	elif args.format == "xml":
		for vr in vrs:
			vr.print_xml()
	else:
		print("Nepodporovaný formát %s" % args.format)
		exit(1)


if __name__ == "__main__":
		sys.exit(main())

