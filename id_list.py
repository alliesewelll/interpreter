from tokenizer import SYMBOLS, TOK_ID

class IdList:
    def __init__(self):
        self.ids = []
    def parse(self, scanner, context, declaring = False):
        if scanner.getToken() != TOK_ID:
            raise Exception("Expected identifier")
        
        name = scanner.idName()
        
        if declaring:
            if name in context.declared:
                raise Exception(f"Identifier {name} already declared")
            context.declared.add(name)
        else:
            if name not in context.declared:
                raise Exception(f"Identifier {name} not declared")
        
        self.ids.append(name)
        scanner.skipToken()
        
        while scanner.getToken() == SYMBOLS[","]:
            scanner.skipToken()
            
            if scanner.getToken() != TOK_ID:
                raise Exception("Expected identifier")
            
            name = scanner.idName()
            if declaring:
                if name in context.declared:
                    raise Exception(f"Identifier {name} already declared")
                context.declared.add(name)
            else:
                if name not in context.declared:
                    raise Exception(f"Identifier {name} not declared")
                
            self.ids.append(name)
            scanner.skipToken()
            
    def print(self):
        print(", ".join(self.ids), end="")