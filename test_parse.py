from tokenizer import Tokenizer
from parse_context import ParseContext
from prog import Prog

scanner = Tokenizer("tests/t4.core")
ctx = ParseContext()
p = Prog()

p.parse(scanner, ctx)
p.print(1)
print("Declared:", ctx.declared)