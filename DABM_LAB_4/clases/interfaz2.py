import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elementos de una interfaz")
        self.setGeometry(100,100,500,500)

        # Insertar una imagen
        self.label_image = QLabel(self)
        self.label_image.setGeometry(50,50,225,225) # valor 1: inicio en x, valor 2: inicio en y, valor 3: ancho en x, valor 4: ancho en y
        pixmap = QPixmap("DABM_LAB_4/archivos/logo.png")
        self.label_image.setPixmap(pixmap)

        # Crear un menú de selección (ComboBox)
        self.label_combo = QLabel("Día de la semana", self)
        self.label_combo.setGeometry(50,280,110,20)
        self.combo_dias = QComboBox(self)
        self.combo_dias.setGeometry(50,310,100,25)
        self.combo_dias.addItems(["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"])

        # Crear grupo de botones de opción de género
        self.label_radio = QLabel("Género:", self)
        self.label_radio.setGeometry(50,340,100,20)
        self.radio_masculino = QRadioButton("Masculino", self)
        self.radio_masculino.setGeometry(50,360,100,20)
        self.radio_femenino = QRadioButton("Femenino", self)
        self.radio_femenino.setGeometry(50,380,100,20)   

        # Crear casillas de verificación para las opciones de salud
        self.label_checkbox = QLabel("Salud:", self)
        self.label_checkbox.setGeometry(250,280,100,20)
        self.checkbox_diabetes = QCheckBox("Diabetes", self)
        self.checkbox_diabetes.setGeometry(250,300,100,20)
        self.checkbox_hipertension = QCheckBox("Hipertensión", self)
        self.checkbox_hipertension.setGeometry(250,320,100,20)   

def load_stylesheet2():
    return """
        QWidget {
            background-color: Thistle;
        }
        QLabel{
            font-size: 14px;
            color: Teal;
        }
        QLineEdit{
            background-color: LightBlue;
            border: 1px solid Magenta;
            padding: 3px;
            font-size: 14px;
        }
        QComboBox{
            background-color: Salmon;
            color: #FFFFFF;
            border: 1px solid Yellow;
            padding: 5px;
            font-size: 14px;
        }
    """