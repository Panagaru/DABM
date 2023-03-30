import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
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

        self.setLayout(layout)

    def auth(self):
        # print('Botón pulsado')
        username = self.edit_username.text()
        password = self.edit_password.text()

        if self.validate_credentials(username, password):
            x = 1
        else:
            x = 0
        return(x)

    def validate_credentials(self,username,password):
        return (username == "usuario" and password == "password")

    app = QApplication(sys.argv)

def load_stylesheet():
    return """
        QWidget {
            background-color: LightGreen;
            box-shadow: 5px 5px 5px #FFFFFF;
        }
        QLabel{
            font-size: 14px;
            color: DarkOrchid;
        }
        QLineEdit{
            background-color: LightBlue;
            border: 1px solid Magenta;
            padding: 3px;
            font-size: 14px;
        }
        QPushButton{
            background-color: Salmon;
            color: SeaGreen;
            border: 1px solid Yellow;
            padding: 5px;
            font-size: 14px;
        }
        QPushButton:hover{
            background-color: Yellow;
            border: 1px solid Salmon;
        }
    """

# if __name__=='__main__':
#     app = QApplication(sys.argv)

#     stylesheet = load_stylesheet()
#     app.setStyleSheet(stylesheet)

#     login_window = LoginWindow()
#     login_window.show()

#     sys.exit(app.exec())
