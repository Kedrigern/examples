#!/usr/bin/env bash
# Title: Search in PDFs
# Author: Ondřej Profant, 2011
# Email: ondrej.profant -at- gmail.com
# Licence: GPL
# Search pattern in all pdf files in actual directory. Use pdftotext for convert - it`s main limit of this script.
# Copy script to  ~/.gnome2/nautilus-scripts  if you would use it from Nautilus file manager.


target=""
match=0

if [ $# -eq 1 ]; then
        target=$1
else
        target=`zenity --entry --text "Zadejte hledané slovo:"`
fi;

for i in *.pdf; do
        if pdftotext $i; then
                count=`grep -c  "${target}" "${i%.pdf}.txt"`
                echo -e "${i}\t${count}" >> res.tmp
                if [ $match -eq 0 -o $count -ne 0 ]; then
                        echo -e "${count}\t\t$i";
                fi;
                rm "${i%.pdf}.txt"
        else
                echo Fail at "$i";
                exit 1;
        fi;
done;

res=`cat res.tmp`;
rm -f res.tmp

myfile=`zenity --list --title="Výsledky vyhledávání" --separator='\t' --column="Soubor" --column="Počet výskytů" ${res}`;

if [ $? -eq 0 ]; then
        evince ${myfile};
fi;
