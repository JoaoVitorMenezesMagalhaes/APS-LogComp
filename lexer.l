%{
#include "parser.tab.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
%}


%%

[ \t\r]+      { /* ignore whitespace */ }

"function"   { return FUNCTION; }
"class"      { return CLASS; }
"if"         { return IF; }
"else"       { return ELSE; }
"in"         { return IN; }
"while"      { return WHILE; }
"species"    { return SPECIES; }
"is"         { return IS; }
"herbivore"  { return HERBIVORE; }
"carnivore"  { return CARNIVORE; }
"omnivore"   { return OMNIVORE; }
"mammal"     { return MAMMAL; }
"bird"       { return BIRD; }
"reptile"    { return REPTILE; }
"fish"       { return FISH; }


"="                     { return ASSIGN; }
"=="                    { return EQ; }
"not"                   { return NOT; }
"+"                     { return PLUS; }
"-"                     { return MINUS; }
"*"                     { return MULT; }
"/"                     { return DIV; }
"&&"                    { return AND; }
"||"                    { return OR; }
">"                     { return GT; }
"<"                     { return LT; }


"("          { return LBRACKET; }
")"          { return RBRACKET; }
"!"          { return PRINT; }
":"          { return COLON; }
","          { return COMMA; }


\n            { return NEWLINE; }
[a-zA-Z_][_a-zA-Z0-9]*   { return IDENTIFIER; }
[0-9]+                  { return INTEGER; }
\"(\\.|[^\"\n])*\"    { return STRING; }

.                       printf("Unknown token!\n"); yyterminate();
%%
