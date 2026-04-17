from parse_utils import expect
from id_list import IdList
from tokenizer import RESERVED_KEYWORDS, SYMBOLS, TOK_ID

class InStmt:
    def __init__(self):
        self.id_list = None
        
    def parse(self, scanner, context):
        expect(scanner, RESERVED_KEYWORDS["read"])
        self.id_list = IdList()
        self.id_list.parse(scanner, context, declaring=False)
        expect(scanner, SYMBOLS[";"])
        
    def print(self, indent = 0):
        print("    " * indent + "read" + " ", end="")
        self.id_list.print()
        print(";")
    
    def execute(self, runtime):
        for name in self.id_list.ids:
            value = runtime.read_next()
            runtime.set_value(name, value)