from tokenizer import RESERVED_KEYWORDS, SYMBOLS
from parse_utils import expect
from id_list import IdList

class OutStmt:
    def __init__(self):
        self.id_list = None
        
    def parse(self, scanner, context):
        expect(scanner, RESERVED_KEYWORDS["write"])
        self.id_list = IdList()
        self.id_list.parse(scanner, context, declaring=False)
        expect(scanner, SYMBOLS[";"])
    
    def print(self, indent = 0):
        print("    " * indent + "write" + " ", end="")
        self.id_list.print()
        print(";")
        
    def execute(self, runtime):
        for name in self.id_list.ids:
            value = runtime.get_value(name)
            print(f"{name} = {value}")