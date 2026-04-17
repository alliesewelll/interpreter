from parse_utils import expect
#from Expr import Expr
from tokenizer import TOK_ID

class Assign:
    def __init__(self):
        self.id = None
        self.expr = None
    
    # def parse(self, scanner, context):
    #     self.id = scanner.getID()
    #     scanner.skipToken()
    #     expect(scanner, TOK_ID)
    #     self.expr = Expr()
    #     self.expr.parse(scanner, context)
    
    # def print(self, indent = 0):
    #     print(" " * indent + f"{self.id} = ", end="")
    #     self.expr.print()
    
    # def execute(self, runtime):
    #     value = self.expr.evaluate(runtime)
    #     runtime.setVariable(self.id, value)