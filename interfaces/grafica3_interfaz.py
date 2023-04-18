# import pyqtgraph.examples
# pyqtgraph.examples.run()

import sys
from PyQt6.QtWidgets import *
import pyqtgraph as pg
import numpy as np

class ECGViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Viso de ECG")

        layout = QVBoxLayout()

        self.plotWidget = pg.PlotWidget()
        layout.addWidget(self.plotWidget)

        controlslayout = QHBoxLayout()
        self.startButton = QPushButton("Iniciar")
        self.stopButton = QPushButton("Detener")
        controlslayout.addWidget(self.startButton)
        controlslayout.addWidget(self.stopButton)

        layout.addLayout(controlslayout)

        self.setLayout(layout)

        self.plotWidget.setYRange(-1.5, 1.5)
        self.plotWidget.showGrid(x=True, y=True)
        self.plotData = self.plotWidget.plot()

        self.startButton.clicked.connect(self.startECG)
        self.stopButton.clicked.connect(self.stopECG)

        self.fs = 1000
        self.duration = 10

        self.sample = int(self.fs * self.duration)

        self.time = np.linspace(0,self.duration, self.sample)

        self.ecg = np.sin(2 * np.pi * 50 *self.time) + 0.5 * np.sin(1 * np.pi * 100 * self.time)

    def startECG(self):
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.updateECG)
        self.timer.start(int(1000/self.fs))

    def stopECG(self):
        self.timer.stop()

    def updateECG(self):
        self.plotData.setData(self.time[:len(self.ecg)], self.ecg)
        self.ecg = np.roll(self.ecg,-1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ecg = ECGViewer()
    ecg.show()
    sys.exit(app.exec())
