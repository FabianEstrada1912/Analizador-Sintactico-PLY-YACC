import ply.lex as lex

reservadas = {
    'variable': 'VAR',
    'procedimiento': 'FUNCTION',
    'si': 'IF',
    'regresa': 'RETURN',
    'hasta': 'FOR',
    'imprimir': 'PRINT',
    'iniciar': 'EJECUTABLE',
    'i': 'IT', 
}

tokens = [
    'IGUAL',
    'COMMA',
    'ID',
    'NUMBER',
    'LLIZQUIERDA',
    'LLDERECHA',
    'PARIZQUIERDO',
    'PARDERECHO',
    'IGUALIGUAL',
    'SUMA',
    'RESTA',
    'MULTI',
    'DIV',
    'PYC',
    'MENOR',
    'MAYOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'STRING',
] + list(reservadas.values())


t_IGUAL = r'='
t_COMMA = r','
t_LLIZQUIERDA = r'{'
t_LLDERECHA = r'}'
t_PARIZQUIERDO = r'\('
t_PARDERECHO = r'\)'
t_IGUALIGUAL = r'=='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIV = r'/'
t_PYC = r';'
t_MENOR = r'<'
t_MAYOR = r'>'
t_MAYORIGUAL= r'>='
t_MENORIGUAL= r'<='
t_RETURN = r'regresa'
t_IF = r'si'
t_VAR = r'variable'
t_FUNCTION = r'procedimiento'
t_FOR = r'hasta'
t_PRINT = r'imprimir'
t_EJECUTABLE = r'inciar'
t_IT = r'i'



t_ignore =  ' \t\n' 

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-ZÑ_][a-zA-ZÑ_0-9]*'
    t.type = reservadas.get(t.value,'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t 

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


analizador = lex.lex()
