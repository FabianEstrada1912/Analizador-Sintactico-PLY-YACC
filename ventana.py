import sys
from PyQt5 import uic, QtWidgets
from upch.Lexer import Lexer
from upch.token import (
    Token,
    TokenType
)


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
        lexer: Lexer = Lexer(cadena_codigo)

        lista_token = ""
        while(token := lexer.next_token()) != TA_TOKEN:
            lista_token = lista_token + '+--------------------+--------------------+ \n' + str(token) 
        cabecera = "+--------------------+--------------------+ \n|Token               |Lexema              |"
        final = cabecera + lista_token
        self.salida.setText(final)    
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())