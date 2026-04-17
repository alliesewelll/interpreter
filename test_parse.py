from tokenizer import Tokenizer
from parse_context import ParseContext
from prog import Prog

scanner = Tokenizer("tests/t10.core")
context = ParseContext()
p = Prog()

p.parse(scanner, context)
p.print(1)
print("Declared:", context.declared)