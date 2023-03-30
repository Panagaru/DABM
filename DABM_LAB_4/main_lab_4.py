import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

from clases.interfaz import LoginWindow, load_stylesheet
from clases.interfaz2 import MainWindow
from clases.tables import UserTable

def menu():
        
    if __name__=='__main__':
        app = QApplication(sys.argv)

        stylesheet = load_stylesheet()
        app.setStyleSheet(stylesheet)

        login_window = LoginWindow()
        login_window.show()

        res=LoginWindow.auth()

        print(res)

        # if res == "1":
            # sys.exit(app.exec())
            # if __name__=='__main__':
            #     app = QApplication(sys.argv)

            #     main_window = MainWindow()
            #     main_window.show()

            #     sys.exit(app.exec())

        sys.exit(app.exec())

menu()