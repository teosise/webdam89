from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route("/form_login")
def login():
    return render_template('login_template.html')

@app.route('/form_login')  # Define la ruta para manejar solicitudes GET en '/form_login'
def login():
    # Renderiza la plantilla HTML llamada 'login_template.html' cuando se accede a la ruta '/form_login'
    return render_template('login_template.html')  # Devuelve la plantilla de login para que se muestre en el navegador

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)