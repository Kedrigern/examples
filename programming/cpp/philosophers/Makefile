
FLAGS=-Wall -pedantic -std=c++11
LIBS=-pthread
CC=g++
DEBUG=-DDEBUG
OUTPUT=dpp

build: main philosopher rp globalLogic
	${CC} ${FLAGS} ${LIBS} -o ${OUTPUT} philosopher.o main.o resourcePool.o globalLogic.o

main: rp
	${CC} -c ${FLAGS} ${DEBUG} -o main.o src/main.cpp

globalLogic: rp philosopher
	${CC} -c ${FLAGS} ${DEBUG} -o globalLogic.o src/globalLogic.cpp

philosopher: rp
	${CC} -c ${FLAGS} ${DEBUG} -o philosopher.o src/philosopher.cpp 

rp: 	
	${CC} -c ${FLAGS} ${DEBUG} -o resourcePool.o src/resourcePool.cpp

doc: doc-pdf doc-html

doc-pdf:
	pandoc --standalone --smart --normalize --toc\
		 --latex-engine=xelatex --listings\
		 -t latex -f markdown -o readme.tex readme.md 
	xelatex readme.tex
	xelatex readme.tex
	rm -f *.aux *.toc *.out *.tex

doc-html:
	pandoc --standalone --smart --normalize --toc\
		 -t html5 -f markdown -o readme.html readme.md

clean:
	rm -f *.o *.run *.html *.pdf *.aux *.log *.toc *.out *.tex
