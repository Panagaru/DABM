import sys
import csv
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton

class RegisterWindow(QWidget):
    def __init__(self, ventana, ventana2, ventana3):
        super().__init__()
        self.ventana = ventana
        self.ventana2 = ventana2
        self.ventana3 = ventana3
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Regristro al sistema DABM')
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        label_username = QLabel('Ingresa nuevo usuario (que no contenga caracteres especiales o ñ):')
        layout.addWidget(label_username)

        self.edit_username = QLineEdit()
        layout.addWidget(self.edit_username)

        label_password = QLabel('Ingresa contraseña:')
        layout.addWidget(label_password)

        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.edit_password)

        btn_crear = QPushButton('Crear')
        btn_crear.clicked.connect(self.crear)
        layout.addWidget(btn_crear)

        btn_ingresar = QPushButton('Ingresar')
        btn_ingresar.clicked.connect(self.ingresa)
        layout.addWidget(btn_ingresar)

        self.setLayout(layout)

    def crear(self):
        self.user = self.edit_username.text()
        self.pas = self.edit_password.text()
        self.nuevo = [self.user, self.pas]
        self.new = []
        self.new.append(self.nuevo)
        x = 0
                    
        cwd = os.getcwd()
        archivo = cwd + "/DABM_LAB_4/archivos/usuarios.csv"
        with open(archivo,"r") as file:
            reader = csv.reader(file, delimiter = ',')
            header = next(reader)
            for row in reader:
                if row[0] == self.user:
                    x = 1
        if x == 1:
            self.ventana.show()
        elif x == 0:
            cwd = os.getcwd()
            archivo = cwd + "/DABM_LAB_4/archivos/usuarios.csv"
            with open(archivo, "a", newline="") as file:
                writer = csv.writer(file,delimiter=',')
                writer.writerows(self.new)
            self.ventana3.show()

    def ingresa(self):
        self.ventana2.show()

def load_stylesheet3():
    return """
        QWidget {
            background-color: AntiqueWhite;
        }
        QLabel{
            font-size: 14px;
            color: Black;
        }
        QLineEdit{
            background-color: LightBlue;
            border: 1px solid Black;
            padding: 3px;
            font-size: 14px;
        }
        QPushButton{
            background-color: LightCyan;
            color: Black;
            border: 1px solid SeaGreen;
            padding: 5px;
            font-size: 14px;
        }
        QPushButton:hover{
            background-color: SeaGreen;
            border: 1px solid LightCyan;
        }
    """
