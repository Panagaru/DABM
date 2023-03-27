import serial
import struct
import time
import csv
import os
from clases.sensor import Sensor

arduino = serial.Serial("COM14",9600)

def menu():
        
    print("\tEste programa te ayuda a crear un archivo csv con los valores entregados por un sensor de luminosidad, con los que se controlará el brillo de un LED o la velocidad de un ventilador.")
    sen = Sensor([])

    # Ingresar valor mínimo y máximo del rango
    print("\nIngresa el valor mínimo del sensor (0-5.0):")
    min=float(input())
    print("\nIngresa el valor máximo del sensor (0-5.0):")
    max=float(input())
    print("\n")

    # Crear el archivo csv
    sen.registrar_lectura(min,max)
    sen.archivo()
    
    while True:
        value = arduino.readline().decode().strip() # Valor del sensor
        valor = int((255*float(value)/5)) # Valor del brillo que le doy al led
        valor_led=sen.conversion(valor,min,max) # Valor del brillo que le doy al led de acuerdo al mínimo y máximo valor ingresados
        valor_led=255-valor_led # entre mayor luminosidad, menos ilumina el led
        arduino.write(struct.pack(">B", int(valor_led)))
        print("valor sensor (V):", value)
        # print("valor led (0-255):", valor_led)
        time.sleep(0.1)

menu()