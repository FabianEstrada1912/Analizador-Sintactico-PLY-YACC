from ast import Assign, keyword
from enum import (
    auto,
    Enum,
    unique,
)
from re import T

from typing import Dict, Literal, NamedTuple



@unique
class TokenType(Enum):
    ASSING = auto()
    IF = auto()
    COMAA = auto()
    TA = auto()
    FUNCTION = auto()
    ID = auto()
    ILEGAL = auto()
    INT = auto()
    LLI = auto()
    LLD = auto()
    VAR = auto()
    PI = auto()
    PD = auto()
    IGIG = auto()
    SUMA = auto()
    RESTA = auto()
    RETURN = auto()
    MULTI = auto()
    DIV = auto()
    PYC = auto()
    MEQ = auto()
    MAQ = auto()
    FOR = auto()
    PRINT =  auto()
    IMPORT =  auto()
    STRING =  auto()
    


class Token(NamedTuple):
    token_type : TokenType
    literal : str

    def __str__(self) -> str:
        cadena = "|{:<20}|{:>20}|".format(str(self.token_type.name), str(self.literal))
        #return f'Token: {self.token_type} | Lexema: {self.literal}'
        return cadena


def view_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'variable' : TokenType.VAR,
        'procedimiento' : TokenType.FUNCTION,
        'si' : TokenType.IF,
        'regresa' : TokenType.RETURN,
        'hasta' : TokenType.FOR,
        'imprimir' : TokenType.PRINT,
    }   

    return keywords.get(literal, TokenType.ID) 


