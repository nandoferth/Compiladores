
D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS			(f|F|l|L)
IS			(u|U|l|L)*

%{
#include <stdio.h>
%}

%%
"/*"			{ printf("<Comentario>"); }

"char"			{ printf("<Tipo Dato>"); }
"float"			{ printf("<Tipo Dato>"); }
"double"		{ printf("<Tipo Dato>"); }
"int"			{ printf("<Tipo Dato>"); }
"long"			{ printf("<Tipo Dato>"); }
"short"			{ printf("<Tipo Dato>"); }

"if"			{ printf("<Sentencia Control>"); }
"else"			{ printf("<Sentencia Control>"); }
"switch"		{ printf("<Sentencia Control>"); }
"case"			{ printf("<Sentencia Control>"); }

"do"			{ printf("<Bucle>"); }
"for"			{ printf("<Bucle>"); }
"while"			{ printf("<Bucle>"); }

"auto"			{ printf("<Palabra Reservada>"); }
"break"			{ printf("<Palabra Reservada>"); }
"const"			{ printf("<Palabra Reservada>"); }
"continue"		{ printf("<Palabra Reservada>"); }
"default"		{ printf("<Palabra Reservada>"); }
"enum"			{ printf("<Palabra Reservada>"); }
"extern"		{ printf("<Palabra Reservada>"); }
"goto"			{ printf("<Palabra Reservada>"); }
"register"		{ printf("<Palabra Reservada>"); }
"return"		{ printf("<Palabra Reservada>"); }
"signed"		{ printf("<Palabra Reservada>"); }
"sizeof"		{ printf("<Palabra Reservada>"); }
"static"		{ printf("<Palabra Reservada>"); }
"struct"		{ printf("<Palabra Reservada>"); }
"typedef"		{ printf("<Palabra Reservada>"); }
"union"			{ printf("<Palabra Reservada>"); }
"unsigned"		{ printf("<Palabra Reservada>"); }
"void"			{ printf("<Palabra Reservada>"); }
"volatile"		{ printf("<Palabra Reservada>"); }


{L}({L}|{D})*		{ printf("<ID>"); }

0[xX]{H}+{IS}?		{ printf("<Hexadecimal>"); }
0{D}+{IS}?		{ printf("<Octal>"); }
{D}+{IS}?		{ printf("<Decimal>"); }
L?'(\\.|[^\\'])+'	{ printf("<Caracter>"); }

{D}+{E}{FS}?		{ printf(" <Exponencial> "); }
{D}*"."{D}+({E})?{FS}?	{ printf(" <Real Esponencial> "); }
{D}+"."{D}*({E})?{FS}?	{ printf(" <Real Esponencial> "); }

L?\"(\\.|[^\\"])*\"	{ printf(" <Cadena> "); }

"..."			{ printf(" <Operador> "); }
"--"			{ printf(" <Operador> "); }
"->"			{ printf(" <Operador> "); }

">>="			{ printf(" <Operador Asignacion> "); }
"<<="			{ printf(" <Operador Asignacion> "); }
"="			{ printf(" <Operador Asignacion> "); }
"+="			{ printf(" <Operador Asignacion> "); }
"-="			{ printf(" <Operador Asignacion> "); }
"*="			{ printf(" <Operador Asignacion> "); }
"/="			{ printf(" <Operador Asignacion> "); }
"%="			{ printf(" <Operador Asignacion> "); }
"&="			{ printf(" <Operador Asignacion> "); }
"^="			{ printf(" <Operador Asignacion> "); }
"|="			{ printf(" <Operador Asignacion> "); }
"++"			{ printf(" <Operador Asignacion> "); }

"&&"			{ printf(" <Operador Logico> "); }
"||"			{ printf(" <Operador Logico> "); }
"!"			{ printf(" <Operador Logico> "); }

"?"			{ printf(" <Operador Condicional> "); }
":"			{ printf(" <Operador Condicional> "); }

"<="			{ printf(" <Operador Relacional> "); }
">="			{ printf(" <Operador Relacional> "); }
"=="			{ printf(" <Operador Relacional> "); }
"!="			{ printf(" <Operador Relacional> "); }
"<"			{ printf(" <Operador Relacional> "); }
">"			{ printf(" <Operador Relacional> "); }

"-"			{ printf(" <Operador Aritmetico> "); }
"+"			{ printf(" <Operador Aritmetico> "); }
"*"			{ printf(" <Operador Aritmetico> "); }
"/"			{ printf(" <Operador Aritmetico> "); }
"%"			{ printf(" <Operador Aritmetico> "); }

"&"			{ printf(" <Operador Bit A Bit> "); }
"^"			{ printf(" <Operador Bit A Bit> "); }
"|"			{ printf(" <Operador Bit A Bit> "); }
"~"			{ printf(" <Operador Bit A Bit> "); }
">>"			{ printf(" <Operador Bit A Bit> "); }
"<<"			{ printf(" <Operador Bit A Bit> "); }

";"			{ printf(" <Separador> "); }
","			{ printf(" <Separador> "); }

("{"|"<%")		{ printf(" <Agrupador> "); }
("}"|"%>")		{ printf(" <Agrupador> "); }
"("			{ printf(" <Agrupador> "); }
")"			{ printf(" <Agrupador> "); }
("["|"<:")		{ printf(" <Agrupador> "); }
("]"|":>")		{ printf(" <Agrupador> "); }
"."			{ printf(" <Agrupador> "); }


[ \t\v\n\f]		{ printf("\n"); }
.			{ /* ignore bad characters */ }

%%

