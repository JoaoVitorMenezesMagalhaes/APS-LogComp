%option noyywrap
%s STRING


%{
#include <stdio.h>
#include <stdlib.h>
#include "parser.tab.h"
%}

%%

"+"          { return PLUS; }
"-"          { return MINUS; }
"*"          { return TIMES; }
"/"          { return DIV; }
"="          { return ASSIGN; }
"<"          { return OPEN; }
">"          { return CLOSE; }
"!"          { return NOT; }
":"          { return COLON; }
";"          { return SEMICOLON; }
"("          { return LPAREN; }
")"          { return RPAREN; }
","          { return COMMA; }
"if"         { return IF; }
"else"       { return ELSE; }
"while"      { return WHILE; }
"for"        { return FOR; }
"function"   { return FUNCTION; }
"class"      { return CLASS; }
"species"    { return SPECIES; }
"print"      { return PRINT; }
"true"       { yylval.boolval = 1; return BOOL; }
"false"      { yylval.boolval = 0; return BOOL; }
[0-9]+       { yylval.numval = atoi(yytext); return NUMBER; }
[a-zA-Z][a-zA-Z0-9]* { yylval.strval = strdup(yytext); return IDENTIFIER; }
"\""         { yylval.strval = strdup(yytext+1); BEGIN(STRING); }
<STRING>[^"]* { yylval.strval = strdup(yytext); return STRING; }
<STRING>\"   { BEGIN(INITIAL); return STRING; }
<STRING>\n   { printf("unterminated string\n"); exit(1); }

[ \t\n]      /* skip whitespace */

.            { printf("invalid character\n"); exit(1); }

%%

int yywrap() {
    return 1;
}

