from flask import Blueprint, session, redirect, url_for, abort, render_template
from tareas_flask.database import get_connection

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/usuarios")
def gestionar_usuarios():
    if "usuario_id" not in session or not session.get("es_admin"):
        abort(403)

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, username, es_admin FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("admin_usuarios.html", usuarios=usuarios)


@admin_bp.route("/borrar/<int:id>")
def borrar_usuario(id):
    if "usuario_id" not in session or not session.get("es_admin"):
        abort(403)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("admin.gestionar_usuarios"))


@admin_bp.route("/promover/<int:id>")
def promover_usuario(id):
    if "usuario_id" not in session or not session.get("es_admin"):
        abort(403)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE usuarios SET es_admin = 1 WHERE id = %s",
        (id,)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("admin.gestionar_usuarios"))
