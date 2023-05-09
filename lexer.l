%{
#include "parser.tab.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
%}


%%

"function"   { return FUNCTION; }
"class"      { return CLASS; }
"if"         { return IF; }
"else"       { return ELSE; }
"for"        { return FOR; }
"in"         { return IN; }
"while"      { return WHILE; }
"species"    { return SPECIES; }
"return"     { return RETURN; }
"="          { return ASSIGN; }
"<"          { return LBRACKET; }
">"          { return RBRACKET; }
"\/"         { return NOT; }
"=="         { return EQ; }
"//"          { return DIVIDE; }
"\/="        { return NEQ; }
"&&"         { return AND; }
"||"         { return OR; }
"!"          { return PRINT; }
":"          { return COLON; }
","          { return COMMA; }
"("          { return LPAREN; }
")"          { return RPAREN; }
"["          { return LBRACE; }
"]"          { return RBRACE; }
"+"          { return PLUS; }
"-"          { return MINUS; }
"*"          { return TIMES; }
"'"          { BEGIN(STRING); }
"STRING"     { return STRING; }

[ \t\r]+      { /* ignore whitespace */ }
\n            { return NEWLINE; }
[a-zA-Z][a-zA-Z0-9]* { yylval.strval = yytext; return IDENTIFIER; }
[0-9]+        { yylval.numval = atoi(yytext); return NUMBER; }
.             { printf("Invalid character: %s\n", yytext); exit(1); }

%%
