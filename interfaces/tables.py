import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class UserTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabla de usuarios")
        self.setGeometry(100,100,500,500)

        # Crear tabla
        self.table = QTableWidget(self)
        self.table.setGeometry(50,50,400,400)

        # Leer archivo csv
        with open("interfaces/usuarios.csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            data = [row for row in reader]

            # Agregar datos a la tabla
            headers = ["Nombre", "Contraseña", "Perfil"]
            self.table.setColumnCount(len(headers))
            self.table.setHorizontalHeaderLabels(headers)
            self.table.setRowCount(len(data))

            for i, row in enumerate(data):
                for j, item in enumerate(row):
                    self.table.setItem(i,j,QTableWidgetItem(item))

if __name__=="__main__":
    app = QApplication(sys.argv)

    # stylesheet = load_stylesheet()
    # app.setStyleSheet(stylesheet)

    user_table = UserTable()
    user_table.show()
    sys.exit(app.exec()) 
