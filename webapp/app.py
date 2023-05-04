from flask import Flask, render_template, request
import os
import random
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return(render_template('registro.html', title='Registro de usuarios'))

@app.route('/crearUsuario', methods=['POST'])
def crear():
    if request.method == "POST":
        usuario = request.form['usuario']
        pwd = request.form['pwd']

        directorio = os.path.dirname(__file__)
        archivo = 'static/users.csv'
        ruta = os.path.join(directorio,archivo)

        with open(ruta,'a') as f:
            f.write(usuario+";"+pwd+"\n")

        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        password = request.form['password']

        directorio = os.path.dirname(__file__)
        archivo = 'static/users.csv'
        ruta = os.path.join(directorio,archivo)

        with open(ruta, 'r') as f:
            datos = f.readlines()

        encontrado = False
        for usuarioF in datos:
            datosUsuario = usuarioF.replace("\n","").split(";")
            # print(datosUsuario)
            if (usuario == datosUsuario[0] and password == datosUsuario[1]):
                encontrado = True
                # grafica = crearGrafica()
                crearGrafica()
                # return render_template('menu.html', usuario=usuario, grafica=grafica)
                return render_template('menu.html', usuario=usuario)
        if encontrado ==  False:
            return("Datos invalidos")

@app.route('/monitor')
def monitor():
    temp = random.randint(20,41)

    parametros = getParametros()

    for i in range(0,3):
        if temp >= int(parametros[i][1]) and temp <= int(parametros[i][2]):
            condicion = str(parametros[i][0])

    

    # Comparar

    return (render_template('monitor.html', parametros=parametros, temp=temp, condicion=condicion))

def crearGrafica():
    days = ["Lunes", "Mrates", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    pacientes = [12, 20, 15, 18, 25, 1, 8]

    fig,ax = plt.subplots()
    ax.bar(days, pacientes)
    ax.set_title("Número de pacientes atendidos en una semana")
    ax.set_xlabel("Días de la semana")
    ax.set_ylabel("Número de pacientes")

    directorio = os.path.dirname(__file__)
    archivo = 'static/grafica.png'
    ruta = os.path.join(directorio,archivo)

    plt.savefig(ruta)

    # buf = io.BytesIO()
    # plt.savefig(buf,format='png')
    # buf.seek(0)
    # grafica = base64.b64encode(buf.getvalue()).decode('utf-8')

    # return(grafica)

def getParametros():
    directorio = os.path.dirname(__file__)
    archivo = 'static/parametros.csv'
    ruta = os.path.join(directorio,archivo)
    with open(ruta, 'r') as f:
        lineas = f.readlines()

    datos = []
    for l in lineas:
        l = l.replace("\n","")
        l = l.split(";")
        datos.append(l)
    return(datos)

if __name__=="__main__":
    app.run(debug=True)