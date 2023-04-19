import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import serial
import struct
import time
import csv
import os

arduino = serial.Serial("COM14",9600)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Controlar el brillo de un LED')
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        label_minimo = QLabel('Valor mínimo del sensor (0-5.0):')
        layout.addWidget(label_minimo)

        self.edit_minimo = QLineEdit()
        layout.addWidget(self.edit_minimo)
        self.min = self.edit_minimo.text()

        label_maximo = QLabel('Valor máximo del sensor (0-5.0):')
        layout.addWidget(label_maximo)

        self.edit_maximo = QLineEdit()
        layout.addWidget(self.edit_maximo)
        self.max = self.edit_maximo.text()

        btn_calcular = QPushButton('Calcular')
        btn_calcular.clicked.connect(self.led)
        layout.addWidget(btn_calcular)

        self.setLayout(layout)

    def conversion(self, valor):
        self.valor = valor
        max = self.edit_maximo.text()
        min = self.edit_minimo.text()
        self.minimo = int((255*float(min)/5))
        self.maximo = int((255*float(max)/5))
        if self.valor <= self.minimo:
            val = 0
        elif self.valor >= self.maximo:
            val = 255
        elif ((self.valor > self.minimo)&(self.valor < self.maximo)):
            val = (0 + ((int(self.valor) - self.minimo)*(255-0)/(self.maximo - self.minimo)))
        return(val)

    def led(self):
        while True:
            value = arduino.readline().decode().strip() # Valor del sensor
            valor = int((255*float(value)/5)) # Valor del brillo que le doy al led
            valor_led=self.conversion(valor) # Valor del brillo que le doy al led de acuerdo al mínimo y máximo valor ingresados
            valor_led=255-valor_led # Entre mayor luminosidad, menos ilumina el led
            arduino.write(struct.pack(">B", int(valor_led)))
            print("valor sensor (V):", value)
            time.sleep(0.05)

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

# if __name__=='__main__':
#     app = QApplication(sys.argv)

#     stylesheet = load_stylesheet2()
#     app.setStyleSheet(stylesheet)

#     main_window = MainWindow()
#     main_window.show()

#     sys.exit(app.exec())
