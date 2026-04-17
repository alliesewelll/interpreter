from op import Op
from tokenizer import SYMBOLS

class Term:
    def __init__(self):
        self.first_factors = None
        self.rest_factors = None
        
    def parse(self, scanner, context):
        self.first_factors = Op()
        self.first_factors.parse(scanner, context)
        
        if scanner.getToken() == SYMBOLS["*"]:
            scanner.skipToken()
            self.rest_factors = Term()
            self.rest_factors.parse(scanner, context)
            
    def print(self):
        self.first_factors.print()
        if self.rest_factors is not None:
            print(" * ", end="")
            self.rest_factors.print()
            
    def evaluate(self, runtime):
        left_value = self.first_factors.evaluate(runtime)
        if self.rest_factors is None:
            return left_value
        return left_value * self.rest_factors.evaluate(runtime)