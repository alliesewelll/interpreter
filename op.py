from tokenizer import TOK_ID, TOK_INT, SYMBOLS
from parse_utils import expect

class Op:
    def __init__(self):
        self.kind = None
        self.int_value = None
        self.id_name = None
        self.expr = None
        
    def parse(self, scanner, context):
        token = scanner.getToken()
        
        if token == TOK_INT:
            self.kind = "int"
            self.int_value = scanner.intVal()
            scanner.skipToken()
            
        elif token == TOK_ID:
            name = scanner.idName()
            if name not in context.declared:
                raise Exception(f"Identifier {name} not declared")
            self.kind = "id"
            self.id_name = name
            scanner.skipToken()
            
        elif token == SYMBOLS["("]:
            from expr import Expr
            self.kind = "expr"
            scanner.skipToken()
            self.expr = Expr()
            self.expr.parse(scanner, context)
            expect(scanner, SYMBOLS[")"])
            scanner.skipToken()
        
        else:
            raise Exception("Expected integer, identifier, or parenthesized expression")
        
    def print(self):
        if self.kind == "int":
            print(self.int_value, end="")
        elif self.kind == "id":
            print(self.id_name, end="")
        elif self.kind == "expr":
            print("(", end="")
            self.expr.print()
            print(")", end="")
                
    def evaluate(self, runtime):
        if self.kind == "int":
            return self.int_value
        elif self.kind == "id":
            return runtime.get_value(self.id_name)
        elif self.kind == "expr":
            return self.expr.evaluate(runtime)