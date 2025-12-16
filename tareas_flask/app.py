from tareas_flask.routes.admin import admin_bp
from flask import Flask, redirect, session, url_for
from tareas_flask.routes.auth import auth_bp
from tareas_flask.routes.tareas import tareas_bp
from tareas_flask.routes.api import api_bp

app = Flask(__name__)
app.secret_key = "clave_secreta_super_segura"

# Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(tareas_bp)
app.register_blueprint(api_bp)
app.register_blueprint(admin_bp)


@app.route("/")
def index():
    # Si está logueado, va a tareas
    if "usuario_id" in session:
        return redirect(url_for("tareas.ver_tareas"))
    # Si no, va a login
    return redirect(url_for("auth.login"))
