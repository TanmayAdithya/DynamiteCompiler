from lex import *


def main():
    source = "IF+-123 foo*THEN/"
    lex = Lexer(source)

    token = lex.getToken()

    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lex.getToken()


main()
