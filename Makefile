# Makefile for pmysql
CC = cc -g
LEX = flex
YACC = bison
CFLAGS = -DYYDEBUG=1

all: pmysql

pmysql: pmysql.tab.o pmysql.o
	${CC} -o $@ pmysql.tab.o pmysql.o
	
pmysql.tab.c pmysql.tab.h: pmysql.y
	${YACC} -vd pmysql.y
	
pmysql.c: pmysql.l
	${LEX} -o $*.c $<
	
pmysql.o: pmysql.c pmysql.tab.h

.SUFFIXES: .pgm .l .y .c