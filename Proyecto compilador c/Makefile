a.out: main.o lex.yy.o lenguaje.tab.o
	gcc lenguaje.tab.o lex.yy.o main.o -ll

main.o: main.c lenguaje.tab.c
	gcc -c main.c

lex.yy.o: lex.yy.c
	gcc -c lex.yy.c

lenguaje.tab.o: lenguaje.tab.c
	gcc -c lenguaje.tab.c

lex.yy.c: lenguaje.l lenguaje.tab.c
	flex lenguaje.l

lenguaje.tab.c: lenguaje.y
	bison -d lenguaje.y

clean:
	rm -f a.out main.o lex.yy.o lenguaje.tab.o lex.yy.c lenguaje.tab.c lenguaje.tab.h

run: a.out 
	./a.out