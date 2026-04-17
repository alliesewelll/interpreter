from expr import Expr
from tokenizer import SYMBOLS, SYMBOLS2
from parse_utils import expect

class Cmpr:
    def __init__(self):
        self.left_expr = None
        self.op = None
        self.right_expr = None
        
    def parse(self, scanner, context):
        expect(scanner, SYMBOLS["("])
        
        self.left_expr = Expr()
        self.left_expr.parse(scanner, context)
        
        if scanner.getToken() not in (
            SYMBOLS2["=="], 
            SYMBOLS2["!="], 
            SYMBOLS["<"], 
            SYMBOLS[">"], 
            SYMBOLS2["<="], 
            SYMBOLS2[">="]
        ):
            raise Exception("Expected comparison operator")
        
        self.op = scanner.getToken()
        scanner.skipToken()
        
        self.right_expr = Expr()
        self.right_expr.parse(scanner, context)
        
        expect(scanner, SYMBOLS[")"])
    
    def print(self):
        print("(", end="")
        
        self.left_expr.print()
        
        if self.op == SYMBOLS2["=="]:
            print(" == ", end="")
        elif self.op == SYMBOLS2["!="]:
            print(" != ", end="")
        elif self.op == SYMBOLS["<"]:
            print(" < ", end="")
        elif self.op == SYMBOLS[">"]:
            print(" > ", end="")
        elif self.op == SYMBOLS2["<="]:
            print(" <= ", end="")
        elif self.op == SYMBOLS2[">="]:
            print(" >= ", end="")
        
        self.right_expr.print()
        
        print(")", end="")
        
    def evaluate(self, runtime):
        left_value = self.left_expr.evaluate(runtime)
        right_value = self.right_expr.evaluate(runtime)
        
        if self.op == SYMBOLS2["=="]:
            return left_value == right_value
        elif self.op == SYMBOLS2["!="]:
            return left_value != right_value
        elif self.op == SYMBOLS["<"]:
            return left_value < right_value
        elif self.op == SYMBOLS[">"]:
            return left_value > right_value
        elif self.op == SYMBOLS2["<="]:
            return left_value <= right_value
        elif self.op == SYMBOLS2[">="]:
            return left_value >= right_value
        else:
            raise Exception("Invalid comparison operator")
        