from tokenizer import *
from parse_utils import expect  

class Decl:
    def __init__(self):
        self.ids = []
    
    def parse(self, scanner, context):
        expect(scanner, RESERVED_KEYWORDS["int"])
        
        if scanner.getToken() != TOK_ID:
            raise Exception("Expected identifier after 'int'")
        
        id_name = scanner.idName()
        if id_name in context.declared:
            raise Exception(f"Identifier '{id_name}' already declared")
        context.declared.add(id_name)
        self.ids.append(id_name)   
        scanner.skipToken()
        
        while scanner.getToken() == SYMBOLS[',']:
            scanner.skipToken()
            if scanner.getToken() != TOK_ID:
                raise Exception("Expected identifier after ','")
            id_name = scanner.idName()
            if id_name in context.declared:
                raise Exception(f"Identifier '{id_name}' already declared")
            context.declared.add(id_name)
            self.ids.append(id_name)   
            scanner.skipToken()
            
        expect(scanner, SYMBOLS[';'])
        
    def print(self, indent = 0):
        print("    " * indent + "int " + ", ".join(self.ids) + ";")