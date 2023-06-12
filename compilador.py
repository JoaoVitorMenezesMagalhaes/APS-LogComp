import sys
from abc import abstractmethod  

reservedWords = ["not", "if", "else", "while", "readline", "readln", "String", "Int", "function", "return", "species", "is"]
species_types = ["herbivore", "carnivore", "omnivore", "mammal", "bird", "reptile", "fish"]
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

global ft

class PrePro:
    @staticmethod
    def filter(code):
        line = code.split("\n")
        for i in range(len(line)):
            if "#" in line[i]:
                line[i] = line[i].split("#")[0]
        return "\n".join(line)

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.children = []

    @abstractmethod
    def evaluate(self, st):
        pass

class BinOp(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children 

    def evaluate(self, st):
        esq = self.children[0].evaluate(st)
        dir = self.children[1].evaluate(st)
        if esq[0] == "String" or dir[0] == "String":
            if self.valor == ".":
                return ["String", str(esq[1]) + str(dir[1])]
            elif self.valor == "==":
                if esq[1] == dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == ">":
                if esq[1] > dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == "<":
                if esq[1] < dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == "||":
                if esq[1] or dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == "&&":
                if esq[1] and dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
        
        else:
            if self.valor == "-":
                return ["Int", esq[1] - dir[1]]
            elif self.valor == "+":
                return ["Int", esq[1] + dir[1]]
            elif self.valor == "*":
                return ["Int", esq[1] * dir[1]]
            elif self.valor == "/":
                return ["Int", esq[1] // dir[1]]
            elif self.valor == "==":
                if esq[1] == dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == ">":
                if esq[1] > dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == "<":
                if esq[1] < dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == "||":
                if esq[1] or dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == "&&":
                if esq[1] and dir[1]:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            elif self.valor == ".":
                return ["String", str(esq[1]) + str(dir[1])]
        
class UnOp(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self, st):
        if self.valor ==  "-":
            return ["Int", -self.children[0].evaluate(st)[1]]
        elif self.valor == "!":
            return ["Int", not self.children[0].evaluate(st)[1]]
        return ["Int", self.children[0].evaluate(st)[1]]

class IntVal(Node):
    def __init__(self, valor):
        self.valor = valor

    def evaluate(self, st):
        return ["Int", int(self.valor)]

class StrVal(Node):
    def __init__(self, valor):
        self.valor = valor

    def evaluate(self, st):
        return ["String", self.valor]

class NoOp(Node):
    def __init__(self):
        pass
    
    def evaluate(self,st):
        return None

class Iden(Node):
    def __init__(self, valor):
        self.valor = valor

    def evaluate(self,st):
        
        return st.get(self.valor)

class Print(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self,st):
        return print(self.children[0].evaluate(st)[1])

class Assignment(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children
    
    def evaluate(self,st):
        return st.add(self.children[0].valor, self.children[1].evaluate(st))
    
class Species(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children
    
    def evaluate(self,st):
        return st.add(self.children[0].valor, ["SPECIE_TYPE", str(self.children[1])])

 
class Block(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self,st):
        for child in self.children:
            if hasattr(child, "valor"):
                child.evaluate(st)
                if child.valor == "return":
                    return child.evaluate(st)

class If(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self,st):
        if self.children[0].evaluate(st)[1]:
            self.children[1].evaluate(st)
        elif len(self.children) == 3:
            self.children[2].evaluate(st)

class While(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self,st):
        while self.children[0].evaluate(st)[1]:
            self.children[1].evaluate(st)

class Readline(Node):
    def __init__(self):
        pass

    def evaluate(self,st):
        return ["Int", int(input())]
    
class FuncDec(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self,st):
        ft.create(self.children[0], self)

class FuncCall(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self,st):
        func = ft.get(self.valor)
        if (len(func.children[1])) != len(self.children):
            raise Exception('Wrong number of arguments')
        func_st= SymbleTable()

        if len(self.children) != 0:
            for i in range(len(func.children[1])):
                func_st.add(func.children[1][i].valor, self.children[i].evaluate(st)) 
        ret_block = func.children[2].evaluate(func_st)
        return ret_block

class Return(Node):
    def __init__(self, valor, children):
        self.valor = valor
        self.children = children

    def evaluate(self,st):
        return self.children[0].evaluate(st)


class SymbleTable:
    def __init__(self):
        self.table = {}
    
    def get(self, name):
        return self.table[name]
    
    def add(self, name, valor):
        self.table[name] = valor
            
    

class FuncTable:
    def __init__(self):
        self.table = {}
    
    def get(self, key):
        return self.table[key]
    
    def create (self, key, valor):
        if key in self.table:
            raise Exception('Function already declared')
        self.table[key] = valor
    


class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = self.selectNext()
        
    
    def selectNext(self):
        if self.position >= len(self.source):
            self.next = Token("EOF", None)
            return self.next
        
        elif self.source[self.position].isdigit():
            number = ""
            while self.position < len(self.source) and self.source[self.position].isdigit():
                number += self.source[self.position]
                self.position += 1
            self.next = Token("NUMBER", number)
            return self.next
            
        elif self.source[self.position].isalnum() or self.source[self.position] == "_":
            word = ""
            while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == "_"):
                word += self.source[self.position]
                self.position += 1
            if word in reservedWords:
                if (word == "Int" or word == "String"):
                    self.next = Token("TYPE", word)
                    return self.next
                else :
                    self.next = Token("RESERVED", word)
                    return self.next
            if word in species_types:
                self.next = Token("SPECIES_TYPE", word)
                return self.next
            else:
                self.next = Token("IDEN", word)
                return self.next


        elif self.source[self.position] == '"':
            self.position += 1
            word = ""
            while self.source[self.position] != '"':
                word += self.source[self.position]
                self.position += 1
            self.next = Token("STRING", word)
            self.position += 1
            return self.next


        elif self.source[self.position] == "+":
            self.next = Token("PLUS", "+")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == "-":
            self.next = Token("MINUS", "-")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == "*":
            self.next = Token("MULT", "*")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == "/":
            self.next = Token("DIV", "/")
            self.position += 1
            return self.next

        elif self.source[self.position] == " ":
            self.position += 1
            return self.selectNext()

        elif self.source[self.position] == "{":
            self.next = Token("OBRACK", "{")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == "}":
            self.next = Token("CBRACK", "}")
            self.position += 1
            return self.next

        elif self.source[self.position] == "(":
            self.next = Token("OPEN", "(")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == ")":
            self.next = Token("CLOSE", ")")
            self.position+=1
            return self.next

        elif self.source[self.position] == "\n":
            self.next = Token("NEWLINE", "\n")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == "=":
            if self.source[self.position+1] == "=":
                self.next = Token("EQUAL", "==")
                self.position += 2
                return self.next
            else:
                self.next = Token("ASSIGN", "=")
                self.position += 1
            return self.next

        elif self.source[self.position] == ">":
            self.next = Token("MAIOR", ">")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == "<":
            self.next = Token("MENOR", "<")
            self.position += 1
            return self.next

        elif self.source[self.position] == "|":
            if self.source[self.position+1] == "|":
                self.next = Token("OR", "||")
                self.position += 2
                return self.next

        elif self.source[self.position] == "&":
            if self.source[self.position+1] == "&":
                self.next = Token("AND", "&&")
                self.position += 2
                return self.next

        elif self.source[self.position] == "!":
            self.next = Token("PRINT", "!")
            self.position += 1
            return self.next

        elif self.source[self.position] == ":":
            if self.source[self.position+1] == ":":
                self.next = Token("COLON", "::")
                self.position += 2
                return self.next

        elif self.source[self.position] == ".":
            self.next = Token("CONCAT", ".")
            self.position += 1
            return self.next
        
        elif self.source[self.position] == ",":
            self.next = Token("COMMA", ",")
            self.position += 1
            return self.next

        else:
            raise Exception("Invalid character")

class Parser:
    def __init__(self, source):
        self.tokenizer = Tokenizer(source)

    def parseBlock(self):
        statement = Block("BLOCK", [])
        while self.tokenizer.next.tipo != "EOF":
            statement.children.append(self.parseStatement())
        return statement

    
    def parseStatement(self):



        if self.tokenizer.next.tipo == "NEWLINE":
            self.tokenizer.selectNext()
            return NoOp()
        
        #elif self.tokenizer.next.tipo == "OBRACK":
        #    self.tokenizer.selectNext()
        #    return NoOp()
        
        elif self.tokenizer.next.tipo == "RESERVED" and self.tokenizer.next.valor == "species":
            self.tokenizer.selectNext()
            if self.tokenizer.next.tipo == "IDEN":
                name = self.tokenizer.next.valor
                self.tokenizer.selectNext()
                if self.tokenizer.next.tipo == "RESERVED" and self.tokenizer.next.valor == "is":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.tipo == "SPECIES_TYPE":
                        specie_type = self.tokenizer.next.valor
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.tipo == "NEWLINE":
                            self.tokenizer.selectNext()
                            return Species("SPECIE", [Iden(name), specie_type])
        
        elif self.tokenizer.next.tipo == "PRINT":
            self.tokenizer.selectNext()
            if self.tokenizer.next.tipo == "OPEN":
                self.tokenizer.selectNext()
                to_print = self.parseRelExpression()
                if self.tokenizer.next.tipo == "CLOSE":
                    self.tokenizer.selectNext()
                    return Print("print", [to_print])
                else: 
                    raise Exception("Expected )")
       
        elif self.tokenizer.next.tipo == "RESERVED" and self.tokenizer.next.valor == "while":
            self.tokenizer.selectNext()
            condition = self.parseRelExpression()
            if self.tokenizer.next.tipo == "OBRACK":
                self.tokenizer.selectNext()
                block_while = Block("BLOCK", [])
                while self.tokenizer.next.tipo != "CBRACK":
                    block_while.children.append(self.parseStatement())  
                if self.tokenizer.next.tipo == "CBRACK":
                    self.tokenizer.selectNext()
                    return While("while", [condition, block_while])
        
        elif self.tokenizer.next.tipo == "RESERVED" and self.tokenizer.next.valor == "if":
            
            self.tokenizer.selectNext()
            condition = self.parseRelExpression()
            if self.tokenizer.next.tipo == "OBRACK":
                self.tokenizer.selectNext()
                block_if = Block("BLOCK", [])
                while self.tokenizer.next.tipo != "CBRACK":
                    block_if.children.append(self.parseStatement()) 

                if self.tokenizer.next.tipo == "CBRACK":
                    self.tokenizer.selectNext()

                while self.tokenizer.next.tipo == "NEWLINE":
                    self.tokenizer.selectNext()            
                    
                if self.tokenizer.next.tipo == "RESERVED" and self.tokenizer.next.valor == "else":
                    self.tokenizer.selectNext()
                    
                    if self.tokenizer.next.tipo == "OBRACK":
                        self.tokenizer.selectNext()
                        block_else = Block("BLOCK", [])
                        while self.tokenizer.next.tipo != "CBRACK":
                            block_else.children.append(self.parseStatement())
                        if self.tokenizer.next.tipo == "CBRACK":
                            self.tokenizer.selectNext()
                            return If("if", [condition, block_if, block_else])
                else:
                    return If("if", [condition, block_if])
                

        elif self.tokenizer.next.tipo == "IDEN":
            name = self.tokenizer.next.valor
            self.tokenizer.selectNext()
            if self.tokenizer.next.tipo == 'ASSIGN':
                self.tokenizer.selectNext()
                return Assignment('ASSIGN', [Iden(name), self.parseRelExpression()])
            

            # elif self.tokenizer.next.tipo == "COLON":
            #     self.tokenizer.selectNext()
            #     if self.tokenizer.next.tipo == "TYPE":
            #         _type = self.tokenizer.next.valor
            #         self.tokenizer.selectNext()
            #         if self.tokenizer.next.tipo == "ASSIGN":
            #             self.tokenizer.selectNext()
            #             return VarDec(_type, [Iden(name), self.parseRelExpression()])
            #         else:
            #             if _type == "Int":
            #                 return VarDec(_type, [Iden(name), 0])
            #             elif _type == "String":
            #                 return VarDec(_type, [Iden(name), ""])
            
            elif self.tokenizer.next.tipo == "OPEN":
                self.tokenizer.selectNext()
                params = []
                if self.tokenizer.next.tipo != "CLOSE":
                    params.append(self.parseRelExpression())
                    while self.tokenizer.next.tipo == "COMMA":
                        self.tokenizer.selectNext()
                        params.append(self.parseRelExpression())
                    if self.tokenizer.next.tipo == "CLOSE":
                        self.tokenizer.selectNext()
                        return FuncCall(name, params)
                else:
                    self.tokenizer.selectNext()
                    return FuncCall(name, params)



            else:
                raise Exception("Invalid IDEN")
        
        elif self.tokenizer.next.tipo == "RESERVED" and self.tokenizer.next.valor == "return":
            self.tokenizer.selectNext()
            return Return("return", [self.parseRelExpression()])
        
        elif self.tokenizer.next.tipo == "RESERVED" and self.tokenizer.next.valor == "function":
            self.tokenizer.selectNext()
            name = self.tokenizer.next.valor
            self.tokenizer.selectNext()
            if self.tokenizer.next.tipo == "OPEN":
                self.tokenizer.selectNext()
                params = []
                if self.tokenizer.next.tipo == "IDEN":
                    params.append(self.parseRelExpression())
                    while self.tokenizer.next.tipo == "COMMA":
                        self.tokenizer.selectNext()
                        params.append(self.parseRelExpression())
                
                if self.tokenizer.next.tipo == "CLOSE":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.tipo == "OBRACK":
                        self.tokenizer.selectNext()
                        block = Block("BLOCK", [])
                        while self.tokenizer.next.tipo != "CBRACK":
                            block.children.append(self.parseStatement())
                        if self.tokenizer.next.tipo == "CBRACK":
                            self.tokenizer.selectNext()
                            return FuncDec("Function", [name, params, block])
                
        else:
            print(self.tokenizer.next.tipo) 
            print(self.tokenizer.next.valor)   
            raise Exception("Invalid statement")
                
    
    def parseRelExpression(self):
        result = self.parseExpression()

        while self.tokenizer.next.tipo == "EQUAL" or self.tokenizer.next.tipo == "MAIOR" or self.tokenizer.next.tipo == "MENOR":
            if self.tokenizer.next.valor == "==":
                self.tokenizer.selectNext()
                result = BinOp("==", [result, self.parseExpression()])
            if self.tokenizer.next.valor == ">":
                self.tokenizer.selectNext()
                result = BinOp(">", [result, self.parseExpression()])
            if self.tokenizer.next.valor == "<":
                self.tokenizer.selectNext()
                result = BinOp("<", [result, self.parseExpression()])

        return result
    

    def parseExpression(self):
        result = self.parseTerm()
        
        while self.tokenizer.next.tipo == "PLUS" or self.tokenizer.next.tipo == "MINUS" or self.tokenizer.next.tipo == "OR" or self.tokenizer.next.tipo == "CONCAT":
            if self.tokenizer.next.valor == "+":
                self.tokenizer.selectNext()
                result = BinOp("+", [result, self.parseTerm()])
            if self.tokenizer.next.valor == "-":
                self.tokenizer.selectNext()
                result = BinOp("-", [result, self.parseTerm()])
            if self.tokenizer.next.valor == "||":
                self.tokenizer.selectNext()
                result = BinOp("||", [result, self.parseTerm()])
            if self.tokenizer.next.valor == ".":
                self.tokenizer.selectNext()
                result = BinOp(".", [result, self.parseTerm()])
        return result

    
    def parseTerm(self):
        
        result = self.parseFactor()
        
        while self.tokenizer.next.tipo == "MULT" or self.tokenizer.next.tipo == "DIV" or self.tokenizer.next.tipo == "AND":
            if self.tokenizer.next.valor == "*":
                self.tokenizer.selectNext()
                result = BinOp("*", [result, self.parseFactor()])
            if self.tokenizer.next.valor == "/":
                self.tokenizer.selectNext()
                result = BinOp("/", [result, self.parseFactor()])
            if self.tokenizer.next.valor == "&&":
                self.tokenizer.selectNext()
                result = BinOp("&&", [result, self.parseFactor()])
        return result

    
    def parseFactor(self):
        
        if self.tokenizer.next.tipo == "MINUS":
            self.tokenizer.selectNext()
            return UnOp("-", [self.parseFactor()])
        
        if self.tokenizer.next.tipo == "PLUS":
            self.tokenizer.selectNext()
            return UnOp("+", [self.parseFactor()])

        if self.tokenizer.next.tipo == "NOT":
            self.tokenizer.selectNext()
            return UnOp("!", [self.parseFactor()])
        
        if self.tokenizer.next.tipo == "NUMBER":
            result = int(self.tokenizer.next.valor)
            self.tokenizer.selectNext()
            return IntVal(result)
        
        elif self.tokenizer.next.tipo == "OPEN":
            self.tokenizer.selectNext()
            result = self.parseRelExpression()
            if self.tokenizer.next.tipo == "CLOSE":
                self.tokenizer.selectNext()
                return result
            else:
                raise Exception("Invalid expression")

        elif self.tokenizer.next.tipo == "IDEN":
            x = self.tokenizer.next.valor
            self.tokenizer.selectNext()
            if self.tokenizer.next.tipo == "OPEN":
                self.tokenizer.selectNext()
                params = []
                if self.tokenizer.next.tipo == "CLOSE":
                    self.tokenizer.selectNext()
                    return FuncCall(x, params)
                else:
                    params.append(self.parseRelExpression())
                    while self.tokenizer.next.tipo == "COMMA":
                        self.tokenizer.selectNext()
                        params.append(self.parseRelExpression())
                    if self.tokenizer.next.tipo == "CLOSE":
                        self.tokenizer.selectNext()
                        return FuncCall(x, params)
            else:
                return Iden(x)

        elif self.tokenizer.next.tipo == "RESERVED":
            if self.tokenizer.next.valor == "readline":
                self.tokenizer.selectNext()
                if self.tokenizer.next.tipo == "OPEN":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.tipo == "CLOSE":
                        self.tokenizer.selectNext()
                        return Readline()
                    else:
                        raise Exception("Invalid expression")

        elif self.tokenizer.next.tipo == "STRING":
            result = self.tokenizer.next.valor
            self.tokenizer.selectNext()
            return StrVal(result)

        raise Exception("Invalid expression")


    @staticmethod
    def run(self, st):
        result = self.parseBlock()
        if self.tokenizer.next.tipo != "EOF":
            raise Exception("Invalid expression")

        
        
        return result.evaluate(st)
        
ft = FuncTable()

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        file = f.read()
    code = PrePro.filter(file)
    st = SymbleTable()
    result = Parser.run(Parser(code), st)


