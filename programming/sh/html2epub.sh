#!/usr/bin/env bash
# Author: Ondřej Profant, 2012
# Email: ondrej.profant <> gmail.com
# Licence: GPLv3 http://www.gnu.org/copyleft/gpl.html
# Description: Convert html file into epub. Except standard terminal control provides simple gui (zenity).

# Variables:
install="${HOME}/.local/share/"
version=0.9

# Functions:
function install {
 dependency=true;
 if tidy -v &> /dev/null; then : else dependency=false; fi;
 if pandoc -v &> /dev/null; then : else dependency=false; fi;
 if zenity --version &> /dev/null; then : else dependency=false; fi;
 if $dependency ; then :
 else
  sudo apt-get install zenity pandoc tidy;
 fi;

 cp $0 ${install}
 echo '<svg width="128" height="128" xmlns="http://www.w3.org/2000/svg">
 <!-- Created with SVG-edit - http://svg-edit.googlecode.com/ -->
 <g>
  <title>Layer 1</title>
  <text xml:space="preserve" text-anchor="middle" font-family="serif" font-size="40" id="svg_2" y="40" x="60" stroke-width="0" stroke="#000000" fill="#000000">html</text>
  <text xml:space="preserve" text-anchor="middle" font-family="serif" font-size="40" id="svg_3" y="110" x="60" stroke-width="0" stroke="#000000" fill="#007f00">epub</text>
  <text xml:space="preserve" text-anchor="middle" font-family="serif" font-size="50" id="svg_4" y="80" x="60" stroke-width="0" stroke="#000000" fill="#ff0000">2</text>
 </g>
</svg>' > ${install}icons/html2epub.svg ;
 echo '#!/usr/bin/env xdg-open
[Desktop Entry]
Categories=Utility;
Comment=Convert html to epub. Has simple gui via zenity.
Encoding=UTF-8
Exec='"${install}${0}"'
Icon='"${install}icons/html2epub.svg"'
Name=Html2epub
NoDisplay=false
StartupNotify=true
Terminal=false
Type=Application
' > ${install}applications/html2epub.desktop ;
}

function uninstall {
 rm -f ${install}${0} ;
 rm -f ${install}icons/html2epub.svg ;
 rm -f ${install}applications/html2epub.desktop ;
}

function myHelp {
	echo -e "$0 convert html file to epub. 
Parametrs:
\t-i\t--input\t\t\tInput file.
\t-o\t--output\t\tOutput file
\t-d\t--debug\t\t\tEnable debug.
\t-h\t--help\t\t\tShow help.
\t-v\t--version\t\tShow version.
\t\t--install\t\tInstall this script (icon, menu etc.).
\t\t--uninstall\t\tUninstall (just clean).
\tnone parametrs\t\t\tRun with simple gui.

Author:\t\tOndřej Profant, ondrej.profant <> gmail.com
Homepage:\thttps://gist.github.com/3497222 ";
}

debug="false";
debugPrefix="${0}_debug_info_"

if [ $# -gt 0 ]; then
	while [ $# -gt 0 ]; do
		case $1 in
"-i" | "--input")
	input=$2;
	shift 2;
;;
"-o" | "--output")
	output=$2;
	shift 2;
;;
"-d" | "--debug")
	debug="true";
;;
"--install")
	install;
	exit 0;
;;
"--uninstall" | "--remove")
	uninstall;
	exit 0;
;;
"-h" | "--help")
	myHelp;
	exit 0;
;;
"-v" | "--version")
	echo $version;
 	exit 0;
;;
*)
	echo "Unknow parametr";
	exit 1;
;;
		esac;
	done;
else
	input=$(zenity --title 'Zvolte vstupní html soubor' --file-selection);
	if [ -z $input ];
		then exit 1;
	fi; 
	output=$(zenity --title 'Zadejte výstupní soubor' --file-selection --save);
	if [ -z $output ];
		then exit 1;
	fi;
fi;

cleanXHTML=$( tidy -asxml -utf8 -q "$input" 2> /dev/null; );
# If input is incorect tidy produce blank output
if [ $? -ne 0  ]; then
	cleanXHTML=$(cat $input);
fi;


if $debug; then
	echo "after Tidy:" > "${debugPrefix}1.txt";
	echo $cleanXHTML >> "${debugPrefix}1.txt";
	echo "---- END ----" >> "${debugPrefix}1.txt"; 
fi;

withoutStyle=$( echo $cleanXHTML | sed '/^<style/,/<\/style>/d
 s/class="[a-zA-Z0-9 ]*"//g'); 

if $debug; then
	echo "after sed:" > "${debugPrefix}2.txt";
	echo $withoutStyle >> "${debugPrefix}2.txt";
	echo "---- END ----" >> "${debugPrefix}2.txt";
fi;

echo $withoutStyle | pandoc --smart --normalize -f html -t epub -o "${output}.epub"
