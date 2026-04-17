from term import Term
from tokenizer import SYMBOLS

class Expr:
    def __init__(self):
        self.first_term = None
        self.op = None
        self.rest_terms = None
        
    def parse(self, scanner, context):
        self.first_term = Term()
        self.first_term.parse(scanner, context)
        
        if scanner.getToken() in (SYMBOLS["+"] , SYMBOLS["-"]):
            self.op = scanner.getToken()
            scanner.skipToken()
            
            self.rest_terms = Expr()
            self.rest_terms.parse(scanner, context)

            
            
    def print(self):
        self.first_term.print()
        if self.rest_terms is not None:
            if self.op == SYMBOLS["+"]:
                print(" + ", end="")
            else:
                print(" - ", end="")
            self.rest_terms.print()
            
    def evaluate(self, runtime):
        value = self.first_term.evaluate(runtime)
        if self.rest_terms is None:
            return value
        
        if self.op == SYMBOLS["+"]:
            value += self.rest_terms.evaluate(runtime)
        else:
            value -= self.rest_terms.evaluate(runtime)
        return value