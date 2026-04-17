from parse_utils import expect
from expr import Expr
from tokenizer import SYMBOLS, TOK_ID

class Assign:
    def __init__(self):
        self.id_name = None
        self.expr = None
    
    def parse(self, scanner, context):
        if scanner.getToken() != TOK_ID:
            raise Exception("Expected identifier")
        
        name = scanner.idName()
        if name not in context.declared:
            raise Exception(f"Identifier {name} not declared")
        self.id_name = name
        scanner.skipToken()
        
        expect(scanner, SYMBOLS["="])
        
        self.expr = Expr()
        self.expr.parse(scanner, context)
        
        expect(scanner, SYMBOLS[";"])
    
    def print(self, indent = 0):
        print("    " * indent + f"{self.id_name} = ", end="")
        self.expr.print()
        print(";")
    
    def execute(self, runtime):
        value = self.expr.evaluate(runtime)
        runtime.set_value(self.id_name, value)