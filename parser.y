%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void);
void yyerror(const char *s);
%}

%token IDENTIFIER NUMBER STRING FUNCTION CLASS IF ELSE WHILE FOR IN SPECIES RETURN ASSIGN LBRACKET RBRACKET NOT EQ DIVIDE NEQ AND OR PRINT COLON COMMA LPAREN RPAREN LBRACE RBRACE PLUS MINUS TIMES NEWLINE

%start block

%union {
    int numval;
    char *strval;
}

%%

block:
    statement
    ;

statement:
    assignment
    | conditional
    | print
    | loop
    | species
    | function
    | class
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
    | for_loop
    ;

while_loop:
    WHILE LBRACKET expression RBRACKET COLON block
    ;

for_loop:
    FOR LBRACKET IDENTIFIER IN range RBRACKET COLON block
    ;

range:
    LBRACE NUMBER COLON NUMBER RBRACE

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

class:
    CLASS IDENTIFIER COLON block
    ;

print:
    PRINT LBRACKET if_expression RBRACKET
    ;

species:
    SPECIES LBRACKET IDENTIFIER RBRACKET COLON attribute_list
    ;

attribute_list:
    attribute
    | attribute_list COMMA attribute
    ;

attribute:
    IDENTIFIER ASSIGN literal
    ;

literal:
    STRING
    | NUMBER
    ;

expression:
    condition
    | expression OR condition
    ;

condition:
    term
    | condition EQ term
    | condition NOT term
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
    | LPAREN if_expression RPAREN
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
