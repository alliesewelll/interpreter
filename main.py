import sys
from tokenizer import Tokenizer
from prog import Prog
from parse_context import ParseContext
from runtime_context import RuntimeContext

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <program_file> <data_file>")
        sys.exit(1)
    
    program_file = sys.argv[1]
    data_file = sys.argv[2]
    
    try:
        scanner = Tokenizer(program_file)
        parse_context = ParseContext()
        prog = Prog()
        
        prog.parse(scanner, parse_context)
        prog.print()
        
        runtime_context = RuntimeContext(data_file)
        prog.execute(runtime_context)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()