import sys
import csv
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton

class LoginWindow(QWidget):
    def __init__(self, ingresar, registrar, ventana4):
        super().__init__()
        self.ingresar = ingresar
        self.registrar = registrar
        self.ventana4 = ventana4
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Ingreso al sistema DABM')
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        label_username = QLabel('Usuario:')
        layout.addWidget(label_username)

        self.edit_username = QLineEdit()
        layout.addWidget(self.edit_username)

        label_password = QLabel('Contraseña:')
        layout.addWidget(label_password)

        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.edit_password)

        btn_ingresar = QPushButton('Ingresar')
        btn_ingresar.clicked.connect(self.auth)
        layout.addWidget(btn_ingresar)

        btn_registrar = QPushButton('Registrar')
        btn_registrar.clicked.connect(self.regis)
        layout.addWidget(btn_registrar)

        self.setLayout(layout)

    def auth(self):
        username = self.edit_username.text()
        password = self.edit_password.text()

        if self.validate_credentials(username, password):
            self.ingresar.show()
            self.close()
        else:
            self.ventana4.show()

    def validate_credentials(self,username,password):
        self.user = "hola"
        self.pas = "contra"
        cwd = os.getcwd()
        archivo = cwd + "/DABM_LAB_4/archivos/usuarios.csv"
        with open(archivo,"r") as file:
            reader = csv.reader(file, delimiter = ',')
            header = next(reader)
            for row in reader:
                if row[0] == username:
                    self.user = row[0]
                    self.pas = row[1]
        return(username == self.user and password == self.pas)

    def regis(self):
        self.registrar.show()

def load_stylesheet():
    return """
        QWidget {
            background-color: Lavender;
        }
        QLabel{
            font-size: 14px;
            color: Black;
        }
        QLineEdit{
            background-color: LightBlue;
            border: 1px solid Black;
            border-radius: 10;
            padding: 3px;
            font-size: 14px;
        }
        QPushButton{
            background-color: LightCyan;
            color: Black;
            border: 1px solid SeaGreen;
            border-radius: 10;
            padding: 5px;
            font-size: 14px;
        }
        QPushButton:hover{
            background-color: SeaGreen;
            border: 1px solid LightCyan;
            border-radius: 10;
        }
    """

# if __name__=='__main__':
#     app = QApplication(sys.argv)

#     stylesheet = load_stylesheet()
#     app.setStyleSheet(stylesheet)

#     login_window = LoginWindow()
#     login_window.show()

#     sys.exit(app.exec())
