all:main.o module.o
	gcc main.o module.o -o main
	make cleanobj
main.o:main.c module.h
	gcc -I . -c main.c
module.o:module.c module.h
	gcc -I . -c module.c
cleanobj:
	rm *.o
clean:
	rm main

