NAME=HelloWorld
BuildDir=build

all: hello

clean:
	rm -rf $(BuildDir)
	rm -rf doc

hello:
	mkdir -p $(BuildDir)/classes
	javac -sourcepath src -d $(BuildDir)/classes src/keddie/*.java

jar: hello
	mkdir -p $(BuildDir)/jar
	jar cfe $(BuildDir)/jar/$(NAME).jar keddie.$(NAME) -C build/classes .
	chmod +x $(BuildDir)/jar/*.jar

doc:
	javadoc -d doc -charset utf-8 keddie src/*/*.java

run: hello
	java -cp $(BuildDir)/classes keddie.$(NAME) # test

