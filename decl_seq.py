from tokenizer import *
from decl import Decl

class DeclSeq:
    def __init__(self):
        self.decls = []
        
    def parse(self, scanner, context):
        if scanner.getToken() != RESERVED_KEYWORDS["int"]:
            raise Exception("Expected declaration sequence")
        
        while scanner.getToken() == RESERVED_KEYWORDS["int"]:
            curr_decl = Decl()
            curr_decl.parse(scanner, context)
            self.decls.append(curr_decl)
            
    def print(self, indent = 0):
        for decl in self.decls:
            decl.print(indent)