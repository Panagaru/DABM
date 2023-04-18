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
from clases.tables import UserTable

def menu():

    if __name__=='__main__':
        app = QApplication(sys.argv)
        
        stylesheet = load_stylesheet()
        app.setStyleSheet(stylesheet)

        main_window = MainWindow()
        register_window = RegisterWindow()

        login_window = LoginWindow(main_window, register_window)
        login_window.show()

        sys.exit(app.exec())

menu()