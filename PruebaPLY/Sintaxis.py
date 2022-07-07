from PruebaPLY.Lexico import tokens, analizador
from sys import stdin
import ply.yacc as yacc
import re
import os
import codecs

precedence = (
    ('right','ID','IF','FOR', 'PRINT'),
    ('right','IGUAL'),
    ('right','IGUALIGUAL'),
    ('left','MAYOR','MENOR'),
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIV'),
    ('left','PARIZQUIERDO','PARDERECHO'),
    ('left','LLIZQUIERDA','LLDERECHA'),
)

nombres = {}



   

def p_f(t):
    '''f : FUNCTION fm'''
    print("funcion")
    

def p_fm(t):
    '''fm : EJECUTABLE PARIZQUIERDO PARDERECHO bc'''
    print("ejecutable")

def p_bc(t):
    '''bc : LLIZQUIERDA comp'''
    print ("bloque codigo")
def p_comp(t):
    '''
    comp : if LLDERECHA
          | for LLDERECHA
          | print LLDERECHA
          | asg LLDERECHA
    '''
    print("complementos")

def p_if(t):
    '''if : IF PARIZQUIERDO eif PARDERECHO PYC compif'''
    print("if")    

def p_eif(t):
    '''eif : ID o NUMBER'''
    print("expresion if")

def p_compif(t):
    '''
    compif : if
            | for
            | print 
            | asg
            | empty
    '''
    print("complemento if y demas")
    
def p_o(t):
    ''' 
    o : MENOR
       | MAYOR
       | MAYORIGUAL
       | MENORIGUAL
       | IGUALIGUAL 
    
    ''' 
    print("operadores")           

def p_for(t):
    '''for : FOR PARIZQUIERDO efor PARDERECHO PYC compif'''
    print("for")

def p_efor(t):
    '''efor : ID op NUMBER'''
    print("expresion for")

def p_op(t):
    ''' op : MENOR '''
    print("operador for")

def p_print(t):
    '''print : PRINT PARIZQUIERDO comprint PARDERECHO PYC compif'''
    print("impresion")

def p_comprint(t):
    '''
    comprint : STRING con
              | ID
    '''   
    print("complemento impresion")

def p_con(t):
    '''con : SUMA ID
            | empty
    ''' 
    print("concatenacion")  

def p_asg(t):
    '''asg : VAR ID compasg PYC compif'''
    print("asignacion")

def p_compasg(t):
    '''
    compasg : IGUAL valor 
             | empty 
    '''
    print("complemento asignacion")

def p_valor(t):
    '''
    valor : ID
           | NUMBER   
    '''
    print("valor asignacion")

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
                resultado_gramatica.append(str(gram) + '\n')
    
    return resultado_gramatica

