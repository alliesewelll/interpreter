from tokenizer import RESERVED_KEYWORDS, TOK_ID
from stmt import Stmt

class StmtSeq:
    def __init__(self):
        self.stmts = []
        
    def parse(self, scanner, context):
        if not self.starts_stmt(scanner.getToken()):
            raise Exception("Expected statement sequence")
        while self.starts_stmt(scanner.getToken()):
            curr_stmt = Stmt()
            curr_stmt.parse(scanner, context)
            self.stmts.append(curr_stmt)
            
    def print(self, indent = 0):
        for stmt in self.stmts:
            stmt.print(indent)
            
    def execute(self, runtime):
        for stmt in self.stmts:
            stmt.execute(runtime)
     
    # Helper function       
    def starts_stmt(self, token):
        return token == TOK_ID or token in (
            RESERVED_KEYWORDS["if"], 
            RESERVED_KEYWORDS["while"], 
            RESERVED_KEYWORDS["read"],
            RESERVED_KEYWORDS["write"],
        )