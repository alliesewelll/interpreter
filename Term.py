from factor import Factor
from tokenizer import SYMBOLS

class Term:
    def __init__(self):
        self.first_factors = None
        self.rest_factors = []
        
    def parse(self, scanner, context):
        self.first_factor = Factor()
        self.first_factor.parse(scanner, context)
        
        while scanner.getToken() == SYMBOLS["*"]:
            scanner.skipToken()
            factor = Factor()
            factor.parse(scanner, context)
            self.rest_factors.append(factor)
            
    def print(self):
        self.first_factor.print()
        for factor in self.rest_factors:
            print(" * ", end="")
            factor.print()
            
    def evaluate(self, runtime):
        value = self.first_factor.evaluate(runtime)
        for factor in self.rest_factors:
            value *= factor.evaluate(runtime)
        return value