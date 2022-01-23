from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

# establecemos una clave secreta para que nuestra app pueda usar sesiones
app.secret_key = '0ad3cc8dfb44979d50f601f835c891571b8215006b025f3cb8167791f49c4060'

# nuestra ruta de índice manejará la representación de nuestro formulario
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # aquí agregamos dos propiedades a la sesión para almacenar el nombre y el correo electrónico
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # Nunca renderices una plantilla en una solicitud POST
    # En su lugar, redirigiremos a nuestra ruta de índice
    return redirect("/show")

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)