# APS-LogComp

## EBNF da linguagem

```
BLOCK = {STATEMENT} ;

ASSIGNMENT = IDENTIFIER "=" EXPRESSION ;

STATEMENT = ( ASSIGNMENT | CONDITIONAL | PRINT | LOOP | SPECIES | λ), "\n" ; 

CONDITIONAL = "if" "<" EXPRESSION ">" ":" BLOCK ["else" BLOCK] ;

LOOP = WHILE_LOOP | FOR_LOOP ;

WHILE_LOOP = "while" "<" EXPRESSION ">" ":" BLOCK ;

FOR_LOOP = "for" "<" IDENTIFIER "in" RANGE ">" ":" BLOCK ;

RANGE = "[" NUMBER ":" NUMBER "]" ;

FUNCTION = "function" IDENTIFIER "<" [ PARAMETERS ] ">" ":" BLOCK ;

PARAMETERS = IDENTIFIER, {"," IDENTIFIER} ;

CLASS = "class" IDENTIFIER ":" BLOCK ;

PRINT = "!" "<" EXPRESSION ">" ; 

SPECIES = "species" "<" IDENTIFIER ">" ":" ATTRIBUTE_LIST ";" ;

ATTRIBUTE_LIST = ATTRIBUTE, {"," ATTRIBUTE} ;

ATTRIBUTE = IDENTIFIER "=" LITERAL ;

LITERAL = STRING | NUMBER ;

IDENTIFIER = LETTER, {LETTER | DIGIT} ;

LETTER = (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z) ;

DIGIT = (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9) ;

NUMBER = DIGIT, {DIGIT} ;

STRING = "'" , {CHAR}, "'" ;

CHAR = (LETTER | DIGIT | " " | "-" | "_" | "." | "," | "!" | "?") ;

EXPRESSION = TERM, {("+" | "-"), TERM} ;

EXPRESSION = CONDITION, { ("||" | "&&"), CONDITION } ;

CONDITION = TERM, { ("<" | ">" | "==" | "!"), TERM } ;

TERM = FACTOR, {("*" | "/"), FACTOR} ;

FACTOR = {("+" | "-"), FACTOR} | IDENTIFIER | NUMBER | ("(", EXPRESSION, ")") ;
```

# Exemplo de uso da linguagem 

```ruby
species <tiger>:
  color = "orange"
  size = 3.3
  diet = "carnivore"
;

species <elephant>:
  color = "gray"
  size = 4.5
  diet = "herbivore"
;

! <"Tigers are " + tiger.size + " meters long and " + tiger.color + " and eat " + tiger.diet + ".">
! <"Elephants are " + elephant.size + " meters long and " + elephant.color + " and eat " + elephant.diet + ".">
```