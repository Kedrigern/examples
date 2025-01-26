
## Basic convetions

* Public class `foo` is in file `foo.java`
* Compiled is into `foo.class`

## What missing

* callbacks (pointer at function etc.)
* functors
* anonymous function, you can create anonymous class:

```
Comparator<String> c = new Comparator<String>() {
    int compare(String s, String s2) { ... }
};
```
* default parametrs
* syntax `var` (shortcut to full class name in declaration)
* getters and setters (just regular function, no special syntax)
* preprocesor directives
* yield keyword

## IDE

### Eclipse

* Lang to en: `echo 'osgi.nl=en' >> ~/.eclipse/org.eclipse.platform_*_linux_gtk_x86_64/configuration/config.ini`
* Show line numbers: Window > Preferences > General > Editors > Text Editors > Show line numbers

### Intellij IDEA

* More flexible than eclipse
* Easy work with custom structure (Makefile and many packages)

## Compilation
Example Makefile:

```
NAME=Main
PACKAGES=Main
DocDir=doc

all: main

clean:
        rm -f *.class $(NAME).jar

main:
        javac -Xlint:unchecked *.java
        jar -cfm $(NAME).jar Manifest.txt *.class
        chmod +x $(NAME).jar

doc:
	javadoc -d $(DocDir) -charser utf-8 -sourcepath src/ $(PACKAGES)
```
And in Manifest.txt we declare entry point of app:
```
Main-Class: Main
```
~                                

## Language

### StdLib
System: exit, in, out, err, currentTimeMillis

java.util.* : 
	ArrayList<T>, Stack<T>, LinkedList<T>, ArrayDeque<T>, PriorityQueue<E>, Map<K,V>
	Arrays: asList<T>, sort, binarySearch
	Scanner: Scanner(System.in), hasNext, next, nextByte, nextInt, nextDouble

java.lang.* :
	StringBuilder

Careful in generic type is Integer, not int.
