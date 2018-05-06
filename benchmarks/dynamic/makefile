CC=g++
CFLAGS=-std=c++17

INCLUDECADMIUM=-I ../../cadmium/include


.PHONY: check_folder clean_files clean

all: check_folder build/main.o
	$(CC) -o bin/TOPMODEL build/main.o 

check_folder:
	mkdir -p build
	mkdir -p bin

build/main.o: ports.hpp empty_atomic.hpp
	time $(CC) -g -c $(CFLAGS) $(INCLUDECADMIUM) main.cpp -o build/main.o

clean_files:
	rm main.cpp
	rm ports.hpp

clean:
	-for d in bin;  do (cd $$d; rm -f TOPMODEL *~ ); done
	-for d in build; do (cd $$d; rm -f *.o *~ ); done