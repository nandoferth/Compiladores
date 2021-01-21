
#include "lenguaje.tab.h"

int main () {

  // yylex();   lexico 
  yyparse();  // sintactico 

  return 0;
}