from cmpr import Cmpr
from parse_utils import expect
from tokenizer import SYMBOLS

class Cond:
    def __init__(self):
        self.kind = None
        self.cmpr = None
        self.left = None
        self.right = None
    
    def parse(self, scanner, context):
        token = scanner.getToken()
        if token == SYMBOLS["!"]:
            self.kind = "not"
            scanner.skipToken()
            self.left = Cond()
            self.left.parse(scanner, context)
            
        elif token == SYMBOLS["["]:
            scanner.skipToken()
            
            self.left = Cond()
            self.left.parse(scanner, context)
            
            token = scanner.getToken()
            if token == SYMBOLS["&&"]:
                self.kind = "and"
            elif token == SYMBOLS["||"]:
                self.kind = "or"
            else:
                raise Exception("Expected && or ||")
            
            scanner.skipToken()
            
            self.right = Cond()
            self.right.parse(scanner, context)
            
            expect(scanner, SYMBOLS["]"])
        
        else:
            self.kind = "cmpr"
            self.cmpr = Cmpr()
            self.cmpr.parse(scanner, context)
            
    def print(self):
        if self.kind == "not":
            print("!", end="")
            self.left.print()
        elif self.kind == "and":
            print("[", end="")
            self.left.print()
            print(" && ", end="")
            self.right.print()
            print("]", end="")
        elif self.kind == "or":
            print("[", end="")
            self.left.print()
            print(" || ", end="")
            self.right.print()
            print("]", end="")
        elif self.kind == "cmpr":
            self.cmpr.print()
    
    def evaluate(self, runtime):
        if self.kind == "not":
            return not self.left.evaluate(runtime)
        elif self.kind == "and":
            return self.left.evaluate(runtime) and self.right.evaluate(runtime)
        elif self.kind == "or":
            return self.left.evaluate(runtime) or self.right.evaluate(runtime)
        elif self.kind == "cmpr":
            return self.cmpr.evaluate(runtime)
        else:
            raise Exception("Invalid condition")