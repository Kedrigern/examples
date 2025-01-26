#!/usr/bin/env python3
"""
Fix epubs generate by Google docs.
In this epubs are inline styles.
This script removes this inline styles.

requirements.txt:
- EbookLib
"""

__version__ = "v0.2.2"
__author__ = "Ondřej Profant"

import os
import re
import sys
import argparse
import ebooklib
from typing import List
from ebooklib import epub
import tkinter as tk
from tkinter import filedialog, messagebox

def copyNameWith(name: str) -> str:
	return re.sub(r'([\w-]*).epub', r'\1-clean.epub', name)

def load_epub(filename: str) -> ebooklib.epub.EpubBook:
	try:
		return epub.read_epub(filename)
	except(FileNotFoundError):
		sys.exit('File not found: ' + filename)
	except(IsADirectoryError):
		sys.exit('File is directory:: ' + filename)
	except(ebooklib.epub.EpubException):
		sys.exit('File is not valid epub: ' + filename)

def get_content_file(ebook: ebooklib.epub.EpubBook) -> List[ebooklib.epub.EpubHtml]:
	return [f for f in ebook.items if isinstance(f, ebooklib.epub.EpubHtml)]

def preview(filename: str, chars = 1500) -> None:
	ebook = load_epub(filename)
	texts = get_content_file(ebook)
	for t in texts:
		print(':: TITLE :: %s, %s ; first %d chars:' % (t.id, t.title, chars))
		print(t.content[:chars].decode('UTF-8'))

def fix(filename: str, newname: str) -> None:
	remove1 = r'( class="[a-zA-Z0-9 ]*"| style="[a-zA-Z0-9:; -]*")'
	remove2 = r'(<span>|</span>)'
	remove3 = r'<style>[a-zA-Z0-9:; -]*</style>'
	ebook = load_epub(filename)
	texts = get_content_file(ebook)
	for i, t in enumerate(texts):
		t1 = re.sub(remove1, r'', t.content.decode('UTF-8'))
		t2 = re.sub(remove2, r'', t1)
		t3 = re.sub(remove3, r'', t2)
		# TODO: for some reason without " " there is no content
		texts[i].set_content(" " + t3)
	epub.write_epub(newname, ebook)

def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, epilog='Author: ' + __author__ + ', version: ' + __version__)
	sub = parser.add_subparsers(dest='subparser_name')
	parser_g = sub.add_parser('gui', help='Run with simple GUI.')
	parser_g.add_argument('-o', '--out', default=None, help='Filename of fixed file.')
	parser_v = sub.add_parser('view', help='Only preview of epub for quick visual analytics.')
	parser_v.add_argument('infile', help='Input file (epub with inline styles)')
	parser_f = sub.add_parser('fix', help='Replace in-line styles.')
	parser_f.add_argument('-o', '--out', help='Filename of fixed file.')
	parser_f.add_argument('infile', help='Input file (epub with inline styles)')
	args = parser.parse_args()

	if args.subparser_name == None:
		parser.print_help()
	elif args.subparser_name == 'gui':
		root = tk.Tk()
		root.withdraw()
		infile = filedialog.askopenfilename(
				filetypes=[('Epub', "*.epub")],
				initialdir=os.path.expanduser('~') )
		if not infile:
			messagebox.showerror('Chyba', 'Nevybrali jste žádný soubor.')
			sys.exit('File not chosen')
	else:
		infile = args.infile

	if args.subparser_name == 'view':
			preview(infile)
	elif args.subparser_name in ['fix', 'gui']:
		if not args.out:
			outfile = copyNameWith(infile)
		fix(infile, outfile)
		if args.subparser_name == 'gui':
			messagebox.showinfo('Podařilo se', 'Podařilo se. Soubor:\n%s byl úspěšně opraven jako soubor: \n%s' % (infile, outfile))

if __name__ == '__main__':
	main()
