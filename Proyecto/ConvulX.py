from flask import Flask, render_template, request
import os

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

@app.route('/menu')
def menu():
    return render_template('menu.html')

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
                return render_template('menu.html', usuario=usuario)
        if encontrado ==  False:
            return("Datos invalidos")

@app.route('/frecuencia')
def frecuencia():
    return render_template('frecuencia.html')

@app.route('/dormir')
def dormir():
    return render_template('dormir.html')

@app.route('/medicamentos')
def medicamentos():
    return render_template('medicamentos.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/que')
def que():
    return render_template('que.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

if __name__=="__main__":
    app.run(debug=True)