%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char* msg);
int yylex(void);

%}

%start BLOCK

%token IDENTIFIER NUMBER STRING LOWER_THAN_ELSE UNARY

%%

BLOCK:
    | BLOCK STATEMENT
    ;

STATEMENT:
      ASSIGNMENT '\n'
    | CONDITIONAL '\n'
    | PRINT '\n'
    | LOOP '\n'
    | SPECIES '\n'
    ;

ASSIGNMENT:
      IDENTIFIER '=' EXPRESSION
    ;

CONDITIONAL:
      IF_EXPRESSION ':' BLOCK %prec LOWER_THAN_ELSE
    | IF_EXPRESSION ':' BLOCK ELSE_EXPRESSION
    ;

IF_EXPRESSION:
      '<' EXPRESSION '>'
    ;

ELSE_EXPRESSION:
      "else" ':' BLOCK
    ;

LOOP:
      WHILE_LOOP
    | FOR_LOOP
    ;

WHILE_LOOP:
      "while" '<' EXPRESSION '>' ':' BLOCK
    ;

FOR_LOOP:
      "for" '<' IDENTIFIER "in" RANGE '>' ':' BLOCK
    ;

RANGE:
      '[' NUMBER ':' NUMBER ']'
    ;

PRINT:
      '!' '<' EXPRESSION '>'
    ;

SPECIES:
      "species" '<' IDENTIFIER '>' ':' ATTRIBUTE_LIST ';'
    ;

ATTRIBUTE_LIST:
      ATTRIBUTE
    | ATTRIBUTE ',' ATTRIBUTE_LIST
    ;

ATTRIBUTE:
      IDENTIFIER '=' LITERAL
    ;

LITERAL:
      STRING
    | NUMBER
    ;

EXPRESSION:
      TERM
    | TERM '+' EXPRESSION
    | TERM '-' EXPRESSION
    ;

TERM:
      FACTOR
    | FACTOR '*' TERM
    | FACTOR '/' TERM
    ;

FACTOR:
      IDENTIFIER
    | NUMBER
    | '(' EXPRESSION ')'
    | '+' FACTOR %prec UNARY
    | '-' FACTOR %prec UNARY
    ;

%%

void yyerror(const char* msg)
{
    fprintf(stderr, "Error: %s\n", msg);
    exit(1);
}

int main(int argc, char** argv)
{
    yyparse();
    return 0;
}
