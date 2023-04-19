import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import csv
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

from clases.interfaz import LoginWindow, load_stylesheet
from clases.interfaz2 import MainWindow, load_stylesheet2
from clases.registrar import RegisterWindow, load_stylesheet3
from clases.ventana import VentanaWindow, load_stylesheet4
from clases.ventana2 import Ventana2Window, load_stylesheet5
from clases.ventana3 import Ventana3Window, load_stylesheet6
from clases.ventana4 import Ventana4Window, load_stylesheet7

def menu():

    if __name__=='__main__':
        app = QApplication(sys.argv)
        
        stylesheet = load_stylesheet()
        app.setStyleSheet(stylesheet)

        main_window = MainWindow()
        ventana_window = VentanaWindow()
        ventana2_window = Ventana2Window()
        ventana3_window = Ventana3Window()
        ventana4_window = Ventana4Window()
        register_window = RegisterWindow(ventana_window, ventana2_window, ventana3_window)

        login_window = LoginWindow(main_window, register_window, ventana4_window)
        login_window.show()

        sys.exit(app.exec())

menu()