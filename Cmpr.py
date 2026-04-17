from expr import Expr
from tokenizer import SYMBOLS

class Cmpr:
    def __init__(self):
        self.left_expr = None
        self.op = None
        self.right_expr = None
        
    def parse(self, scanner, context):
        self.left_expr = Expr()
        self.left_expr.parse(scanner, context)
        
        if scanner.getToken() not in (
            SYMBOLS["=="], 
            SYMBOLS["!="], 
            SYMBOLS["<"], 
            SYMBOLS[">"], 
            SYMBOLS["<="], 
            SYMBOLS[">="]
        ):
            raise Exception("Expected comparison operator")
        
        self.op = scanner.getToken()
        scanner.skipToken()
        
        self.right_expr = Expr()
        self.right_expr.parse(scanner, context)
    
    def print(self):
        self.lext_expr.print()
        
        if self.op == SYMBOLS["=="]:
            print(" == ", end="")
        elif self.op == SYMBOLS["!="]:
            print(" != ", end="")
        elif self.op == SYMBOLS["<"]:
            print(" < ", end="")
        elif self.op == SYMBOLS[">"]:
            print(" > ", end="")
        elif self.op == SYMBOLS["<="]:
            print(" <= ", end="")
        elif self.op == SYMBOLS[">="]:
            print(" >= ", end="")
        
        self.right_expr.print()
        
    def evaluate(self, runtime):
        left_value = self.left_expr.evaluate(runtime)
        right_value = self.right_expr.evaluate(runtime)
        
        if self.op == SYMBOLS["=="]:
            return left_value == right_value
        elif self.op == SYMBOLS["!="]:
            return left_value != right_value
        elif self.op == SYMBOLS["<"]:
            return left_value < right_value
        elif self.op == SYMBOLS[">"]:
            return left_value > right_value
        elif self.op == SYMBOLS["<="]:
            return left_value <= right_value
        elif self.op == SYMBOLS[">="]:
            return left_value >= right_value
        else:
            raise Exception("Invalid comparison operator")
        