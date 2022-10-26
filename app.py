from flask import Flask, render_template, redirect, request, session, url_for
from flask_session import Session

from DataBaseConnection import selectQuery, selectVariableQuery
from helper import login_required

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():  # put application's code here
    return redirect(url_for('login'))

@app.route("/operator")
@login_required
def operator():
    query = "SELECT * FROM Registro INNER JOIN Producto on Registro.idProducto = Producto.id ORDER BY fecha LIMIT 2"
    rows = selectQuery(query)
    return render_template("operator.html", nombre=rows[0][5], foto=rows[0][7],  fotoSig=rows[1][7], id=rows[0][1], descripcion=rows[0][6], cantidad=rows[0][2], siguiente=rows[1][5])

@app.route("/administrator")
@login_required
def administrator():
    return render_template("admin.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return "must provide username"
        elif not request.form.get("password"):
            return "must provide password"

        tmp = request.form.get("username")
        tmp2 = request.form.get("password")
        rows = selectVariableQuery("SELECT id, rol FROM Usuario WHERE user = %s and password = %s", [tmp, tmp2])

        if len(rows) != 1:
            return "invalid username and/or password"

        session["user_id"] = rows[0][0]

        # Redirect user to home page
        if rows[0][1]== "Operario":
            return redirect("/operator")
        else:
            return redirect("/administrator")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.run()
