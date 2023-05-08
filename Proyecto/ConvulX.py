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
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        rh = request.form['rh']
        eps = request.form['eps']
        direccion = request.form['direccion']
        usuario = request.form['usuario']
        pwd = request.form['pwd']

        directorio = os.path.dirname(__file__)
        archivo = 'static/users.csv'
        ruta = os.path.join(directorio,archivo)

        with open(ruta,'a') as f:
            f.write(nombre+";"+apellido+";"+rh+";"+eps+";"+direccion+";"+usuario+";"+pwd+"\n")

        directorio_c = os.path.dirname(__file__)
        archivo_c = 'static/contactos.csv'
        ruta_c = os.path.join(directorio_c,archivo_c)

        for i in range(0,3):
            with open(ruta_c,'a') as f:
                f.write(usuario+";"+pwd+";"+" "+";"+" "+";"+" "+";"+" "+"\n")

        return (render_template('login.html'))

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
            if (usuario == datosUsuario[5] and password == datosUsuario[6]):
                encontrado = True

                directorio = os.path.dirname(__file__)
                archivo = 'static/verificar.csv'
                ruta = os.path.join(directorio,archivo)

                with open(ruta, 'w') as f:
                    f.write(usuario+";"+password+"\n")

                return render_template('menu.html')
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

    directorio_v = os.path.dirname(__file__)
    archivo_v = 'static/verificar.csv'
    ruta_v = os.path.join(directorio_v,archivo_v)

    with open(ruta_v, 'r') as f:
        datos = f.readlines()
        for usuariov in datos:
            datosUsuariov = usuariov.replace("\n","").split(";")
            usuario = datosUsuariov[0]
            password = datosUsuariov[1]
    
    directorio = os.path.dirname(__file__)
    archivo = 'static/users.csv'
    ruta = os.path.join(directorio,archivo)

    with open(ruta, 'r') as f:
        datos = f.readlines()

    for usuarioF in datos:
        datosUsuario = usuarioF.replace("\n","").split(";")
        if (usuario == datosUsuario[5] and password == datosUsuario[6]):
            nombre =  datosUsuario[0]
            apellido =  datosUsuario[1]
            rh = datosUsuario[2]
            eps =  datosUsuario[3]
            direccion = datosUsuario[4]

    directorioc = os.path.dirname(__file__)
    archivoc = 'static/contactos.csv'
    rutac = os.path.join(directorioc,archivoc)

    with open(rutac, 'r') as f:
        datosc = f.readlines()

    c = 0

    for usuarioc in datosc:
        datosUsuarioc = usuarioc.replace("\n","").split(";")
        if (usuario == datosUsuarioc[0] and password == datosUsuarioc[1]):
            c = c+1
    
    co = 0
    if (c<=3):
        for usuarioc in datosc:
            datosUsuarioc = usuarioc.replace("\n","").split(";")
            if (usuario == datosUsuarioc[0] and password == datosUsuarioc[1]):
                co = co+1
                if (co==1):
                    conta =  datosUsuarioc[2]
                    contaap =  datosUsuarioc[3]
                    parentesco = datosUsuarioc[4]
                    telefono =  datosUsuarioc[5]
                if (co==2):
                    conta2 =  datosUsuarioc[2]
                    contaap2 =  datosUsuarioc[3]
                    parentesco2 = datosUsuarioc[4]
                    telefono2 =  datosUsuarioc[5]
                if (co==3):
                    conta3 =  datosUsuarioc[2]
                    contaap3 =  datosUsuarioc[3]
                    parentesco3 = datosUsuarioc[4]
                    telefono3 =  datosUsuarioc[5]
                    
    co = 1
    if (c>3):
        for usuarioc in datosc:
            datosUsuarioc = usuarioc.replace("\n","").split(";")
            if (usuario == datosUsuarioc[0] and password == datosUsuarioc[1]):
                # co = co+1
                
                if (c==4):
                    if (" " != datosUsuarioc[2]):
                        if (co==3):
                            co = co+1
                            conta =  datosUsuarioc[2]
                            contaap =  datosUsuarioc[3]
                            parentesco = datosUsuarioc[4]
                            telefono =  datosUsuarioc[5]
                    if (" " == datosUsuarioc[2]):
                        if (co==1):
                            co = co+1
                            conta3 =  datosUsuarioc[2]
                            contaap3 =  datosUsuarioc[3]
                            parentesco3 = datosUsuarioc[4]
                            telefono3 =  datosUsuarioc[5]
                    if (" " == datosUsuarioc[2]):
                        if (co==2):
                            co = co+1
                            conta2 =  datosUsuarioc[2]
                            contaap2 =  datosUsuarioc[3]
                            parentesco2 = datosUsuarioc[4]
                            telefono2 =  datosUsuarioc[5]
                            
                            
                if (c==5):
                    if (" " != datosUsuarioc[2]):
                        if (co==2):
                            co = co+1
                            conta =  datosUsuarioc[2]
                            contaap =  datosUsuarioc[3]
                            parentesco = datosUsuarioc[4]
                            telefono =  datosUsuarioc[5]
                    if (" " != datosUsuarioc[2]):
                        if (co==3):
                            co = co+1
                            conta2 =  datosUsuarioc[2]
                            contaap2 =  datosUsuarioc[3]
                            parentesco2 = datosUsuarioc[4]
                            telefono2 =  datosUsuarioc[5]
                    if (" " == datosUsuarioc[2]):
                        if (co==1):
                            co = co+1
                            conta3 =  datosUsuarioc[2]
                            contaap3 =  datosUsuarioc[3]
                            parentesco3 = datosUsuarioc[4]
                            telefono3 =  datosUsuarioc[5]
                        
                   
                if (c==6):   
                    if (" " != datosUsuarioc[2]):
                        if (co==1):
                            conta =  datosUsuarioc[2]
                            contaap =  datosUsuarioc[3]
                            parentesco = datosUsuarioc[4]
                            telefono =  datosUsuarioc[5]
                        if (co==2):
                            conta2 =  datosUsuarioc[2]
                            contaap2 =  datosUsuarioc[3]
                            parentesco2 = datosUsuarioc[4]
                            telefono2 =  datosUsuarioc[5]
                        if (co==3):
                            conta3 =  datosUsuarioc[2]
                            contaap3 =  datosUsuarioc[3]
                            parentesco3 = datosUsuarioc[4]
                            telefono3 =  datosUsuarioc[5]
                        co = co+1

    return render_template('usuario.html', nombre=nombre, apellido=apellido, rh=rh, eps=eps, direccion=direccion, conta=conta, contaap=contaap, parentesco=parentesco, telefono=telefono, conta2=conta2, contaap2=contaap2, parentesco2=parentesco2, telefono2=telefono2, conta3=conta3, contaap3=contaap3, parentesco3=parentesco3, telefono3=telefono3)

@app.route('/nuevo_contacto', methods=['POST'])
def contacto():

    directorio_v = os.path.dirname(__file__)
    archivo_v = 'static/verificar.csv'
    ruta_v = os.path.join(directorio_v,archivo_v)

    with open(ruta_v, 'r') as f:
        datos = f.readlines()
        for usuariov in datos:
            datosUsuariov = usuariov.replace("\n","").split(";")
            usuario = datosUsuariov[0]
            password = datosUsuariov[1]

    if request.method == "POST":
        conta = request.form['conta']
        contaap = request.form['contaap']
        parentesco = request.form['parentesco']
        telefono = request.form['telefono']

        directorio = os.path.dirname(__file__)
        archivo = 'static/contactos.csv'
        ruta = os.path.join(directorio,archivo)

        # with open(ruta, 'r') as f:
        #     datosd = f.readlines()
        #     for usuariod in datosd:
        #         datosUsuario = usuariod.replace("\n","").split(";")
        #         if (usuario == datosUsuario[0] and password == datosUsuario[1]):
        #             if (""== datosUsuario[2]):
        with open(ruta,'a') as d:
            d.write(usuario+";"+password+";"+conta+";"+contaap+";"+parentesco+";"+telefono+"\n")

        return (render_template('usuario.html'))

if __name__=="__main__":
    app.run(debug=True)