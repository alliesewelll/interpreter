import sys

RESERVED_KEYWORDS = {
    "program" : 1, 
    "begin" : 2,
    "end" : 3,
    "int" : 4,
    "if" : 5,
    "then" : 6,
    "else" : 7,
    "while" : 8,
    "loop" : 9,
    "read" : 10,
    "write" : 11,
}

SYMBOLS = {
    ";" : 12,
    "," : 13,
    "=" : 14,
    "!" : 15,
    "[" : 16,
    "]" : 17,
    "(" : 20,
    ")" : 21,
    "+" : 22,
    "-" : 23, 
    "*" : 24,
    "<" : 27,
    ">" : 28
}

SYMBOLS2 = {
    "&&" : 18,
    "||" : 19,
    "!=" : 25,
    "==" : 26,
    "<=" : 29,
    ">=" : 30
    
}

TOK_INT = 31
TOK_ID = 32
TOK_EOF = 33
TOK_ERR = 34

class Tokenizer:
    def __init__(self, filename):
        self.reader = open(filename, 'r', encoding='utf-8')
        self.tokens: list[tuple[int, str]] = []
        self.current_token_index = 0
        self.eof_reached = False
        self.tokenizeLine()

    def getToken(self) -> int:
        return self.tokens[self.current_token_index][0]
    
    def skipToken(self):
        t = self.getToken()
        if t in (TOK_EOF, TOK_ERR):
            return
        self.current_token_index += 1
        if self.current_token_index >= len(self.tokens):
            self.tokenizeLine()
            
    def intVal(self) -> int:
        if self.getToken() != TOK_INT:
            raise Exception("Current token is not an integer")
        return int(self.tokens[self.current_token_index][1])  
    
    def idName(self) -> str:
        if self.getToken() != TOK_ID:
            raise Exception("Current token is not an identifier")
        return self.tokens[self.current_token_index][1]
    
    def tokenizeLine(self):
        # Keep reading until we get a non-empty token list or EOF
        while self.eof_reached == False or len(self.tokens) == 0:
            line = self.reader.readline()

            if line == "":
                self.eof_reached = True
                self.tokens = [(33, "EOF")]
                self.current_token_index = 0
                return

            self.tokens = self.scan_line(line)
            self.current_token_index= 0

            # If the line is whitespace-only, keep going
            if len(self.tokens) == 0:
                continue

            # Otherwise we have tokens (or ERR)
            return

    def scan_line(self, line: str) -> list[tuple[int, str]]:
        out: list[tuple[int, str]] = []
        n = len(line)
        j = 0

        while j < n:
            c = line[j]

            # Skip whitespace
            if c.isspace():
                j += 1
                continue

            # 2-char symbols
            if j + 1 < n:
                two = line[j:j+2]
                if two in SYMBOLS2:
                    out.append((SYMBOLS2[two], two))
                    j += 2
                    continue

            # 1-char symbols
            if c in SYMBOLS:
                out.append((SYMBOLS[c], c))
                j += 1
                continue

            # Integer: digit(s)
            if c.isdigit():
                k = j
                while k < n and line[k].isdigit():
                    k += 1
                val = line[j:k]
                out.append((TOK_INT, val))
                j = k
                continue

            # Identifier: uppercase letter, then uppercase/digit
            if "A" <= c <= "Z":
                k = j
                while k < n and (("A" <= line[k] <= "Z") or line[k].isdigit()):
                    k += 1

                # If next char is lowercase, that's illegal token per spec example (e.g., ABCend)
                if k < n and ("a" <= line[k] <= "z"):
                    # consume the rest of that “word-like” chunk to report as one illegal token
                    m = k
                    while m < n and (not line[m].isspace()) and (line[m] not in SYMBOLS):
                        m += 1
                    bad = line[j:m]
                    out.append((TOK_ERR, bad))
                    return out

                val = line[j:k]
                # could be reserved word ONLY if it matches exactly (reserved words are lowercase)
                # so uppercase-start means it's an ID, not reserved.
                out.append((TOK_ID, lex))
                j = k
                continue

            # Reserved word (lowercase start)
            if "a" <= c <= "z":
                k = j
                while k < n and ("a" <= line[k] <= "z"):
                    k += 1
                val = line[j:k]
                if val in RESERVED_KEYWORDS:
                    out.append((RESERVED_KEYWORDS[val], val))
                    j = k
                    continue
                else:
                    # illegal word (misspelled keyword, etc.)
                    out.append((TOK_ERR, val))
                    return out

            # Anything else is illegal
            out.append((TOK_ERR, c))
            return out

        return out


def main():
    if len(sys.argv) != 2:
        print("Usage: python tokenizer.py <inputfile>")
        sys.exit(1)

    tk = Tokenizer(sys.argv[1])
    t = tk.getToken()
    while t != TOK_EOF and t != TOK_ERR:
        tk.skipToken()
        print(t)
        t = tk.getToken()
        if t == TOK_EOF:
            print(t)
            print("Reached EOF.")
            return
        if t == TOK_ERR:
            print(t)
            print(f"Illegal token: {tk.tokens[tk.current_token_index][1]}")
            return


if __name__ == "__main__":
    main()
    
        