from term import Term
from tokenizer import SYMBOLS

class Expr:
    def __init__(self):
        self.first_term = None
        self.ops = []
        self.rest_terms = []
        
    def parse(self, scanner, context):
        self.first_term = Term()
        self.first_term.parse(scanner, context)
        
        while scanner.getToken() in (SYMBOLS["+"] , SYMBOLS["-"]):
            op = scanner.getToken()
            self.ops.append(op)
            scanner.skipToken()
            
            term = Term()
            term.parse(scanner, context)
            self.rest_terms.append(term)
            
            
    def print(self):
        self.first_term.print()
        for i in range(len(self.ops)):
            if self.ops[i] == SYMBOLS["+"]:
                print(" + ", end="")
            else:
                print(" - ", end="")
            self.rest_terms[i].print()
            
    def evaluate(self, runtime):
        value = self.first_term.evaluate(runtime)
        
        for i in range(len(self.ops)):
            next_value = self.rest_terms[i].evaluate(runtime)
            if self.ops[i] == SYMBOLS["+"]:
                value += next_value
            else:
                value -= next_value
        return value