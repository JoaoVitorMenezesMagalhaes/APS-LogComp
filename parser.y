%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void);
void yyerror(const char *s);
%}

%token IDENTIFIER NUMBER STRING NEWLINE
%token FUNCTION IF ELSE WHILE IN SPECIES IS 
%token LBRACKET RBRACKET LBRACE RBRACE PRINT COMMA
%token ASSIGN EQ NOT MULT DIV PLUS MINUS AND OR LT GT
%token HERBIVORE CARNIVORE OMNIVORE MAMMAL BIRD REPTILE FISH

%start program

%%

program:
    statement_list
    ;

block:
    LBRACE statement_list RBRACE
    | LBRACE RBRACE
    ;

statement_list:
    statement
    | statement_list statement
    ;

statement : SPECIES IDENTIFIER IS type
          | IDENTIFIER ASSIGN relexpression
          | PRINT LBRACKET relexpression RBRACKET
          | IF LBRACKET relexpression RBRACKET block
          | IF LBRACKET relexpression RBRACKET block ELSE block
          | WHILE LBRACKET relexpression RBRACKET block 
          | FUNCTION IDENTIFIER LBRACKET parameter_list RBRACKET block
          | IDENTIFIER LBRACKET parameter_list RBRACKET
          | NEWLINE
          ;

parameter_list:
    /* empty */
    | IDENTIFIER
    | parameter_list COMMA IDENTIFIER
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

relexpression: expression EQ expression
             | expression GT expression
             | expression LT expression
             | expression
             ;

expression: term PLUS term
          | term MINUS term
          | term OR term
          | term
          ;
          
term: factor
    | term MULT factor
    | term DIV factor
    | term AND factor
    ;

factor: NUMBER 
    | STRING 
    | IDENTIFIER 
    | PLUS factor
    | MINUS factor
    | NOT factor
    | LBRACKET relexpression RBRACKET
    ;


%%

void yyerror(const char *s) {
    printf("%s\n", s);
}

int main() {
    yyparse();
    return 0;
}
