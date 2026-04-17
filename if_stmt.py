from tokenizer import RESERVED_KEYWORDS, SYMBOLS
from parse_utils import expect
from cond import Cond


class If:
    def __init__(self):
        self.condition = None
        self.then_stmt = None
        self.else_stmt = None
        
    def parse(self, scanner, context):
        from stmt_seq import StmtSeq
        expect(scanner, RESERVED_KEYWORDS["if"])
        self.condition = Cond()
        self.condition.parse(scanner, context)

        expect(scanner, RESERVED_KEYWORDS["then"])
        self.then_stmt = StmtSeq()
        self.then_stmt.parse(scanner, context)
        
        if scanner.getToken() == RESERVED_KEYWORDS["else"]:
            scanner.skipToken()
            self.else_stmt = StmtSeq()
            self.else_stmt.parse(scanner, context)
        
        expect(scanner, RESERVED_KEYWORDS["end"])
        expect(scanner, SYMBOLS[";"])
    
    def print(self, indent = 0):
        print("    " * indent + "if ", end="")
        self.condition.print()
        print(" then")
        self.then_stmt.print(indent + 1)
        if self.else_stmt is not None:
            print("    " * indent + "else")
            self.else_stmt.print(indent + 1)
        print("    " * indent + "end;")
        
    def execute(self, runtime):
        if self.condition.evaluate(runtime):
            self.then_stmt.execute(runtime)
        elif self.else_stmt is not None:
            self.else_stmt.execute(runtime)