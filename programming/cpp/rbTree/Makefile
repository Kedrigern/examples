CFLAGS=-O0 -g -Wall
LDFLAGS=

all: tree

clean:
	rm -f main.o

tree: main.o
	g++ $(LDFLAGS) -o tree main.o

main.o: main.cpp
	g++ -c $(CFLAGS) -o main.o main.cpp
