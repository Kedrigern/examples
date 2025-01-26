#!/usr/bin/env bash
#
# Convert asciidoc file (*.adoc) into markdown.
# Main goal is better processing with file (power of padoc)
# 
# Author: Ondřej Profant
# Dependency: asciidoctor, pandoc

if asciidoctor -v > /dev/null; then
	:
else
	echo "Doinstalujte asciidoc:"
	echo "gem install asciidoc"
	exit
fi;

if pandoc -v > /dev/null; then
	:
else
	echo "Doinstalujte pandoc"
	exit
fi;

if [ -z "$1" ]; then
	echo "Usage: $0 <file>" 
	exit
fi;

input="$1"
output="${1%.adoc}.md"

asciidoctor -b docbook -o - "$input" | pandoc -f docbook -t markdown -o "$output"
