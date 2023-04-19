import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class VentanaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Aviso')
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        label_mensaje = QLabel("Este nombre de usuario ya existe, por favor ingresa otro (que no contenga caracteres especiales o ñ).")
        layout.addWidget(label_mensaje)

        self.setLayout(layout)

def load_stylesheet4():
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