from parse_utils import expect
from tokenizer import RESERVED_KEYWORDS, SYMBOLS
from cond import Cond

class Loop:
    def __init__(self):
        self.condition = None
        self.body = None
        
    def parse(self, scanner, context):
        from stmt_seq import StmtSeq
        expect(scanner, RESERVED_KEYWORDS["while"])
        self.condition = Cond()
        self.condition.parse(scanner, context)  
        
        expect(scanner, RESERVED_KEYWORDS["loop"])
        self.body = StmtSeq()
        self.body.parse(scanner, context)
        
        expect(scanner, RESERVED_KEYWORDS["end"])
        expect(scanner, SYMBOLS[";"])
        
    def print(self, indent = 0):
        print("    " * indent + "while ", end="")
        self.condition.print()
        print(" loop")
        self.body.print(indent + 1)
        print("    " * indent + "end;")
        
    def execute(self, runtime):
        while self.condition.evaluate(runtime):
            self.body.execute(runtime)