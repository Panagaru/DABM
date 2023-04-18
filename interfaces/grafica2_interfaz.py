import sys
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random

class HeartRateMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Monitor de frecuencia cardiaca")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.figure = Figure(figsize=(6,4),dpi=100)
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.canvas)

        self.axes = self.figure.add_subplot(111)
        self.axes.set_ylim(0,200)
        self.x_data = [0]
        self.y_data = [0]

        self.line, = self.axes.plot(self.x_data, self.y_data)

        self.time = self.startTimer(1000)
    
    def timerEvent(self,event):
        self.x_data.append(self.x_data[-1] + 1)
        self.y_data.append(random.randint(60,150))
        self.line.set_data(self.x_data,self.y_data)

        self.axes.set_xlim(max(0,self.x_data[-1] - 50), self.x_data[-1] + 10)

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = HeartRateMonitor()
    monitor.show()
    sys.exit(app.exec())

