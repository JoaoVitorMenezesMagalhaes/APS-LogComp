%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void);
void yyerror(const char *s);
%}

%token IDENTIFIER NUMBER STRING FUNCTION IF ELSE WHILE IN SPECIES IS ASSIGN LBRACKET RBRACKET NOT EQ DIVIDE AND OR PRINT COLON COMMA PLUS MINUS TIMES NEWLINE
%token HERBIVORE CARNIVORE OMNIVORE MAMMAL BIRD REPTILE FISH

%start block

%%

block:
    statement NEWLINE
    ;

statement:
    assignment
    | conditional
    | print
    | loop
    | species   
    | function
    ;

assignment:
    IDENTIFIER ASSIGN if_expression
    ;

if_expression:
    condition COLON block else_block_opt
    ;

conditional:
    IF LBRACKET expression RBRACKET COLON block else_block_opt
    ;

else_block_opt:
    /* empty */
    | ELSE COLON block
    ;

loop:
    while_loop
    ;

while_loop:
    WHILE LBRACKET expression RBRACKET COLON block
    ;

function:
    FUNCTION IDENTIFIER LBRACKET parameters_opt RBRACKET COLON block
    ;

parameters_opt:
    /* empty */
    | parameter_list
    ;

parameter_list:
    IDENTIFIER
    | parameter_list COMMA IDENTIFIER
    ;

print:
    PRINT LBRACKET if_expression RBRACKET
    ;

species:
    SPECIES IDENTIFIER IS type
    ;

type:
    HERBIVORE
    | CARNIVORE
    | OMNIVORE
    | MAMMAL
    | BIRD
    | REPTILE
    | FISH
    ;

expression:
    condition
    | expression OR condition
    ;

condition:
    term
    | condition EQ term
    | NOT term
    ;

term:
    factor
    | term DIVIDE factor
    | term TIMES factor
    ;

factor:
    IDENTIFIER
    | NUMBER
    | STRING
    | LBRACKET expression RBRACKET
    | MINUS factor
    | PLUS factor
    ;

%%

void yyerror(const char *s) {
    printf("%s\n", s);
}

int main() {
    yyparse();
    return 0;
}
