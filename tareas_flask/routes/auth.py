from flask import Blueprint, render_template, request, redirect, url_for, session
from tareas_flask.database import get_connection
from tareas_flask.models.usuario import Usuario, UsuarioAdmin

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if "usuario_id" in session:
        return redirect(url_for("tareas.tareas"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuarios WHERE username = %s AND password = %s",
            (username, password)
        )
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            if user["es_admin"]:
                usuario = UsuarioAdmin(user["id"], user["username"])
            else:
                usuario = Usuario(user["id"], user["username"])

            session["usuario_id"] = usuario.id
            session["es_admin"] = usuario.es_administrador()

            return redirect(url_for("tareas.tareas"))

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if "usuario_id" in session:
        return redirect(url_for("tareas.tareas"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("register.html", error="Campos obligatorios")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT id FROM usuarios WHERE username = %s",
            (username,)
        )

        if cursor.fetchone():
            cursor.close()
            conn.close()
            return render_template("register.html", error="Usuario ya existe")

        cursor.execute(
            "INSERT INTO usuarios (username, password, es_admin) VALUES (%s, %s, %s)",
            (username, password, False)
        )
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
