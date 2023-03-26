# APS-LogComp

## EBNF da linguagem

BLOCK = {STATEMENT} ;

ASSIGNMENT = IDENTIFIER "=" EXPRESSION ;

STATEMENT = ( ASSIGNMENT | CONDITIONAL | PRINT | LOOP | λ), "\n" ; 

CONDITIONAL = "if" "<" EXPRESSION ">" ":" STATEMENT ["else" STATEMENT] ;

LOOP = WHILE_LOOP | FOR_LOOP ;

WHILE_LOOP = "while" "<" EXPRESSION ">" ":" BLOCK ;

FOR_LOOP = "for" "<" IDENTIFIER "in" RANGE ">" ":" BLOCK ;

RANGE = "[" NUMBER ":" NUMBER "]" ;

FUNCTION = "function" IDENTIFIER "<" [ PARAMETERS ] ">" ":" BLOCK ;

PARAMETERS = IDENTIFIER, {"," IDENTIFIER} ;

CLASS = "class" IDENTIFIER ":" BLOCK ;

PRINT = "!" "<" EXPRESSION ">" ; 

IDENTIFIER = LETTER, {LETTER | DIGIT} ;

LETER = (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z) ;

DIGIT = (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9) ;

NUMBER = DIGIT, {DIGIT} ;

EXPRESSION = TERM, {("+" | "-"), TERM} ;

TERM = FACTOR, {("*" | "/"), FACTOR} ;

FACTOR = {("+" | "-"), FACTOR} | IDENTIFIER | NUMBER | ("(", EXPRESSION, ")") ;