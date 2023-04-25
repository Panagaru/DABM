from flask import Flask, render_template, request

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

        with open('static/users.csv','a') as f:
            f.write(usuario+";"+pwd+"\n")

        return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)