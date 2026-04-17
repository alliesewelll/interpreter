from tokenizer import RESERVED_KEYWORDS
from parse_utils import expect
from decl_seq import DeclSeq
from stmt_seq import StmtSeq

class Prog:
    def __init__(self):
        self.decl_seq = None
        self.stmt_seq = None
        
    def parse(self, scanner, context):
        expect(scanner, RESERVED_KEYWORDS["program"])
        
        self.decl_seq = DeclSeq()
        self.decl_seq.parse(scanner, context)
        
        expect(scanner, RESERVED_KEYWORDS["begin"])
        
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse(scanner, context)
        
        expect(scanner, RESERVED_KEYWORDS["end"])
        
    def print(self, indent = 0):
        print("program")
        if self.decl_seq is not None:
            self.decl_seq.print(indent + 1)
        print("begin")
        if self.stmt_seq is not None:
            self.stmt_seq.print(indent + 1)
        print("end")
        
    def execute(self, runtime):
        if self.stmt_seq is not None:
            self.stmt_seq.execute(runtime)