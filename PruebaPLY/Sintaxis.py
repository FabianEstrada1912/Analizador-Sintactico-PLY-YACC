from PruebaPLY.Lexico import tokens, analizador
from sys import stdin
import ply.yacc as yacc
import re
import os
import codecs

precedence = (
    ('right','IGUAL'),
    ('right','IGUALIGUAL'),
    ('left','MAYOR','MENOR'),
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIV'),
    ('right','PARIZQUIERDO','PARDERECHO'),
    ('left','LLIZQUIERDA','LLDERECHA'),
)

nombres = {}
   

def p_f(t):
    '''f : FUNCTION fm'''
    t[0] = t[2]
    print("funcion")
   

def p_fm(t):
    '''fm : EJECUTABLE PARIZQUIERDO PARDERECHO bc'''
    t[0] = t[4]
    print("ejecutable")

def p_bc(t):
    '''bc : LLIZQUIERDA comp'''
    t[0] = t[2]
    print ("bloque codigo")

def p_comp(t):
    '''
    comp : if LLDERECHA
          | for LLDERECHA
          | print LLDERECHA
          | asg LLDERECHA
    '''
    t[0] = t[1]
    print("complementos")

def p_if(t):
    '''if : IF PARIZQUIERDO eif PARDERECHO LLIZQUIERDA compif LLDERECHA'''
    if(t[3]):
        t[0] = t[6]
        print("IF si cumple")
    else:
        t[0] = 0
        print("IF no cumple")
    print("if " + str(t[3]) + str(t[6]))    

def p_eif(t):
    ''' eif : expresion MENOR expresion
            | expresion MAYOR expresion
            | expresion MAYORIGUAL expresion
            | expresion MENORIGUAL expresion
            | expresion IGUALIGUAL expresion '''
    if t[2] == "<" : t[0] = t[1] < t[3]
    elif t[2] == ">" : t[0] = t[1] > t[3]
    elif t[2] == ">=" : t[0] = t[1] >= t[3]
    elif t[2] == "<=" : t[0] = t[1] <= t[3]
    elif t[2] == "==" : t[0] = t[1] == t[3]
    print("expresion if ")


          
def p_for(t):
    '''for : FOR PARIZQUIERDO efor PARDERECHO LLIZQUIERDA compif LLDERECHA'''
    i = 0
    while i < t[3]:
        t[0] = t[6] 
        print(t[0])
        i+=1
    t[0] = t[6]   
    print("for")

def p_efor(t):
    '''efor : IT op expresion'''
    t[0] = t[3]
    print("expresion for")
    

def p_op(t):
    ''' op : MENOR '''
    t[0] = t[1]
    print("operador for")
    

def p_compif(t):
    '''
    compif : if
            | for
            | print 
            | asg
            | empty
    '''
    t[0] = t[1]
    print("complemento if y demas")

def p_print(t):
    '''print : PRINT PARIZQUIERDO comprint PARDERECHO compif'''
    t[0] = t[3]
    print("impresion")
    
def p_comprint(t):
    '''
    comprint : ID
             | STRING con 
    ''' 
    ##| STRING con 
    if (len(t) == 2):
        t[0] = t[1] 
    elif (len(t) == 3):
        t[1].join(str(t[2]))
        t[0] = t[1] 
    
    print("complemento impresion")
   
def p_con(t):
    '''con : SUMA expresion
            | empty
    ''' 
    if (len(t) == 2):
        t[0] = t[1] 
    elif (len(t) == 3):
        t[0] = t[2] 
    print("concatenacion")  

def p_asg(t):
    '''asg : VAR ID IGUAL expresion PYC compif'''
    nombres[t[2]] = t[4]
    """if t[2] not in nombres:
        nombres[t[2]] = t[4]
    else:
        print("Variable Repetida")"""
    t[0] = t[6] 
    print("asignacion")
 
""" def p_compasg(t):
    '''
    compasg : IGUAL valor 
             | empty 
    '''
    t[0] = t[2]
    print("complemento asignacion")

def p_valor(t):
    '''
    valor : ID
           | NUMBER   
    '''
    t[0] = t[1]
    print("valor asignacion")"""

def p_expresion_numero(t):
    'expresion : NUMBER'
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : ID'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0


def p_empty(t):
     'empty :'
     pass    

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = " Error sintactico de tipo {} en el valor {}".format(str(t.type),str(t.value)) 
    else:
        resultado = "Error sintactico {}".format(t)
    resultado_gramatica.append(resultado) 


parser = yacc.yacc()

resultado_gramatica = []

def prueba(data) :
    resultado_gramatica.clear()
    for item in data.splitlines() :
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
    
    return resultado_gramatica

