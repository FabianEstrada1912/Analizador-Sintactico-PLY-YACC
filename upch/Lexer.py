from re import match

from upch.token import (
    Token,
    TokenType,
    view_token_type,
)

class Lexer: 
    
    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0
        
        self._read_character()
    
    def next_token(self) -> Token:
        self._skip_espacio()
        self._skip_salto()

        if match(r"^=$", self._character):
            if self._peek_character() == "=":
                token = self._make_two_character(TokenType.IGIG)
            elif self._peek_character() == ">":
                token = self._make_two_character(TokenType.RETURN)
            else:
                token = Token(TokenType.ASSING, self._character)
        elif match(r"^\"$", self._character):
            if self._peek_ahead_character('"'):
                token = self._make_a_lot_of_character_token(
                    self._character, TokenType.STRING
                )
            else:
                token = Token(TokenType.ILLEGAL, '"')    
        elif match (r'^\+$', self._character):
            token = Token(TokenType.SUMA, self._character)
        elif match(r"^\($", self._character):
            token = Token(TokenType.PI, self._character)
        elif match(r"^\)$", self._character):
            token = Token(TokenType.PD, self._character)
        elif match(r"^{$", self._character):
            token = Token(TokenType.LLI, self._character)
        elif match(r"^}$", self._character):
            token = Token(TokenType.LLD, self._character)
        elif match(r"^,$", self._character):
            token = Token(TokenType.COMAA, self._character)
        elif match(r"^;$", self._character):
            token = Token(TokenType.PYC, self._character)
        elif match(r"^$", self._character):
            token = Token(TokenType.TA, self._character)
        elif match(r'^-$', self._character):
            token = Token(TokenType.RESTA, self._character)
        elif match(r'^\*$', self._character):
            token = Token(TokenType.MULTI, self._character)
        elif match(r'^\/$', self._character):
            token = Token(TokenType.DIV, self._character)
        elif match(r'^>$', self._character):
            token = Token(TokenType.MAQ, self._character)
        elif match(r"^<$", self._character):
            token = Token(TokenType.MEQ, self._character) 
        elif self._is_letter(self._character):
            literal = self._read_id()
            token_type = view_token_type(literal)
            return Token(token_type, literal) 
        elif self._is_number(self._character):
            literal = self._read_number()
            return Token(TokenType.INT, literal)  
        else:     
            token = Token(TokenType.ILEGAL, self._character)
        
        self._read_character()
        
        return token

    def _is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-zA-ZñÑ_]$', character))
    
    
    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character))    

    
    def _read_id(self) -> str:
        initial_position = self._position

        while self._is_letter(self._character):
            self._read_character()

        return self._source[initial_position:self._position]       



    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1

    def _read_number(self) -> str:
        initial_position = self._position

        while self._is_number(self._character):
            self._read_character()

        return self._source[initial_position:self._position]                  

    def _skip_espacio(self) -> None:
        while match(r'^[\s\t]$', self._character):
            self._read_character() 

    def _skip_salto(self) -> None:
        while match(r'\n$', self._character):
            self._read_character()         

    def _peek_character(self) -> str:
        if self._read_position >= len(self._source):
            return ''

        return self._source[self._read_position]  

    def _make_two_character(self, token_type: TokenType) -> Token:
        prefix = self._character
        self._read_character
        suffix = self._character

        return Token(token_type, f'{prefix}{suffix}')     

    def _make_a_lot_of_character_token(self, character: str, token_type: TokenType) -> Token:
        initial_position = self._read_position

        self._read_character()

        while self._character != character:
            self._read_character()

        return Token(
            token_type,
            self._source[initial_position - 1 : self._read_position]
        )


    def _peek_ahead_character(self, character: str) -> bool:
        initial_position = self._read_position

        self._read_character()

        while self._character != character and self._read_position <= len(self._source):
            self._read_character()

        if self._character == character and initial_position != self._read_position:
            self._read_position = initial_position
            return True
        else:
            self._read_position = initial_position
            return False
     