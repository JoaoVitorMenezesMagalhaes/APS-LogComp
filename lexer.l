%{
#include "parser.tab.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
%}


%%

[ \t\r]+      { /* ignore whitespace */ }

"function"   { printf("FUNCTION\n"); return FUNCTION; }
"if"         { printf("IF\n"); return IF; }
"else"       { printf("ELSE\n"); return ELSE; }
"in"         { printf("IN\n"); return IN; }
"while"      { printf("WHILE\n"); return WHILE; }
"species"    { printf("SPECIES\n"); return SPECIES; }
"is"         { printf("IS\n"); return IS; }
"herbivore"  { printf("HERBIVORE\n"); return HERBIVORE; }
"carnivore"  { printf("CARNIVORE\n"); return CARNIVORE; }
"omnivore"   { printf("OMNIVORE\n"); return OMNIVORE; }
"mammal"     { printf("MAMMAL\n"); return MAMMAL; }
"bird"       { printf("BIRD\n"); return BIRD; }
"reptile"    { printf("REPTILE\n"); return REPTILE; }
"fish"       { printf("FISH\n"); return FISH; }


"="                     { printf("ASSIGN\n"); return ASSIGN; }
"=="                    { printf("EQ\n"); return EQ; }
"not"                   { printf("NOT\n"); return NOT; }
"+"                     { printf("PLUS\n"); return PLUS; }
"-"                     { printf("MINUS\n"); return MINUS; }
"*"                     { printf("MULT\n"); return MULT; }
"/"                     { printf("DIV\n"); return DIV; }
"&&"                    { printf("AND\n"); return AND; }
"||"                    { printf("OR\n"); return OR; }
">"                     { printf("GT\n"); return GT; }
"<"                     { printf("LT\n"); return LT; }


"("          { printf("LBRACKET\n"); return LBRACKET; }
")"          { printf("RBRACKET\n"); return RBRACKET; }
"!"          { printf("PRINT\n"); return PRINT; }
"{"          { printf("LBRACE\n"); return LBRACE; }
"}"          { printf("RBRACE\n"); return RBRACE; }
","          { printf("COMMA\n"); return COMMA; }


\n            { return NEWLINE; }
[a-zA-Z_][_a-zA-Z0-9]*   { printf("IDENTIFIER\n"); return IDENTIFIER; }
[0-9]+                  { printf("NUMBER\n"); return NUMBER; }
\"(\\.|[^\"\n])*\"    { printf("STRING\n"); return STRING; }

.                       printf("Unknown token!\n"); yyterminate();
%%

