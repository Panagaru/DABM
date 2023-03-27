import serial
import struct
import time
import csv
import os

class Sensor():
    def __init__(self, lectura_sensor):
        self.lectura_sensor = lectura_sensor

    def conversion(self, valor, minimo, maximo):
        self.valor = valor
        self.minimo = int((255*float(minimo)/5))
        self.maximo = int((255*float(maximo)/5))
        if self.valor <= self.minimo:
            val = 0
        elif self.valor >= self.maximo:
            val = 255
        elif ((self.valor > self.minimo)&(self.valor < self.maximo)):
            val = (0 + ((int(self.valor) - self.minimo)*(255-0)/(self.maximo - self.minimo)))
        return(val)
        
    def registrar_lectura(self, minimo, maximo):
        self.minimo = minimo
        self.maximo = maximo
        self.lista = [str(self.minimo), str(self.maximo)]
        self.lectura_sensor.append(self.lista)

    def archivo(self):
        cwd = os.getcwd()
        ruta = cwd + "/DABM_LAB_3/archivos/"
        ruta = ruta + "/" + "Valores_sensor" + ".csv"
        self.headers = ["Mínimo", "Máximo"]
        with open(ruta, "w", newline="") as file:
            writer = csv.writer(file,delimiter=';')
            writer.writerow(self.headers)
            writer.writerows(self.lectura_sensor)