from tokenizer import *

def expect(scanner, expected_token):
        if scanner.getToken() != expected_token:
            raise Exception(f"Expected token {expected_token} but got {scanner.getToken()}")
        scanner.skipToken()
        