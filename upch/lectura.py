from upch.Lexer import Lexer
from upch.token import (
    Token,
    TokenType
)

TA_TOKEN: Token = Token(TokenType.TA, '')

def start_lectura() -> None:
    while (source := input ('>> ')) != 'exit':
        lexer: Lexer = Lexer(source)

        while(token := lexer.next_token()) != TA_TOKEN: 
            print(token)     