from tokenizer import TOK_ID, RESERVED_KEYWORDS
from assign import Assign
from in_stmt import InStmt
from out_stmt import OutStmt
from if_stmt import If
from loop import Loop

class Stmt:
    def __init__(self):
        self.stmt = None
    
    def parse(self, scanner, context):
        token = scanner.getToken()
        if token == TOK_ID:
            self.stmt = Assign()
            self.stmt.parse(scanner, context)
        elif token == RESERVED_KEYWORDS["read"]:
            self.stmt = InStmt()
            self.stmt.parse(scanner, context)
        elif token == RESERVED_KEYWORDS["write"]:
            self.stmt = OutStmt()
            self.stmt.parse(scanner, context)
        elif token == RESERVED_KEYWORDS["if"]:
            self.stmt = If()
            self.stmt.parse(scanner, context)
        elif token == RESERVED_KEYWORDS["while"]:
            self.stmt = Loop()
            self.stmt.parse(scanner, context)
        else:
            raise Exception("Expected statement")
        
    def print(self, indent = 0):
        self.stmt.print(indent)
    
    def execute(self, runtime):
        self.stmt.execute(runtime)