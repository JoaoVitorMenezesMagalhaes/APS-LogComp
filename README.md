# APS-LogComp

## EBNF da linguagem

```
BLOCK = { STATEMENT } ;

ASSIGNMENT = IDENTIFIER "=" EXPRESSION ;

STATEMENT = ( ASSIGNMENT | CONDITIONAL | PRINT | WHILE_LOOP | FUNCTION | SPECIES | λ ), "\n" ; 

IF = "if" "(" EXPRESSION ")", BLOCK [ "else", BLOCK ] ;

WHILE_LOOP = "while" "(" EXPRESSION ")", BLOCK ;

FUNCTION = "function" IDENTIFIER "(" [ PARAMETERS ] ")", BLOCK ;

PARAMETERS = IDENTIFIER { "," IDENTIFIER } ;

PRINT = "!" "(" EXPRESSION ")" ; 

SPECIE = "specie" IDENTIFIER "is" TYPE;

TYPE = "herbivore" | "carnivore" | "omnivore" | "mammal" | "bird" | "reptile" | "fish" ;

IDENTIFIER = LETTER { LETTER | DIGIT } ;

LETTER = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

NUMBER = DIGIT { DIGIT } ;

STRING = '"' , { CHAR } , '"' ;

CHAR = LETTER | DIGIT | " " | "-" | "_" | "." | "," | "!" | "?" ;

EXPRESSION = CONDITION, { ("||" | "&&"), CONDITION } ;

CONDITION = TERM, { ("<" | ">" | "==" | "not"), TERM } ;

TERM = FACTOR, {("*" | "//"), FACTOR} ;

FACTOR = {("+" | "-"), FACTOR} | IDENTIFIER | NUMBER | "(", EXPRESSION, ")" ;

```

# Exemplo de uso da linguagem 

```ruby

species Dog is mammal
species Sparrow is bird

function bark(){
    !("WOOF WOOF!")
}

if (Dog == "mammal") {
    !("Dog is a mammal")
    bark()
} else {
    !("Dog is not a mammal")
}

if (Dog == Sparrow) {
    !("Dog and Sparrow are the same species")
} else {
    !("Dog and Sparrow are not the same species")
    !(Dog)
    !(Sparrow)
}

```

# Uso do Flex e Bison

```
flex -l lexer.l
bison -dv parser.y 
gcc -o analyzer parser.tab.c lex.yy.c -lfl
./analyzer < exemplo.txt
```