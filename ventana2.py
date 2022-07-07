from lib2to3.pgen2 import token
import sys
from PyQt5 import uic, QtWidgets
from PruebaPLY.Sintaxis import prueba, parser
from upch.token import (
    Token,
    TokenType
)

from PruebaPLY.Lexico import tokens, analizador

TA_TOKEN: Token = Token(TokenType.TA, '')


qtCreatorFile = "lexico.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.boton.clicked.connect(self.iniciar_lexer)

    def iniciar_lexer(self):
        cadena_codigo = self.entrada.toPlainText()
        
        lexico = analizador
        lexico.input(cadena_codigo)
        tok = lexico.token()
        lista_token = ""
        while True:
            tok = lexico.token()
            
            if not tok : break
            lista_token = lista_token + '\n' + str(tok)
        self.salida.setText(lista_token)  

        cad = []
        cont = 0
        for i in prueba(cadena_codigo):
            if(cont == 0):
                cont +=1
            else: 
                cad.append(i)
        

        self.salida.setText(lista_token + str(cad))

        
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())