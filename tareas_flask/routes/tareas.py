from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from tareas_flask.database import get_connection
from tareas_flask.models.tarea import Tarea

tareas_bp = Blueprint("tareas", __name__)

@tareas_bp.route("/tareas", methods=["GET", "POST"])
def tareas():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        descripcion = request.form.get("descripcion")
        if descripcion:
            cursor.execute(
                "INSERT INTO tareas (descripcion, usuario_id) VALUES (%s, %s)",
                (descripcion, session["usuario_id"])
            )
            conn.commit()

    cursor.execute(
        "SELECT id, descripcion, usuario_id FROM tareas WHERE usuario_id = %s",
        (session["usuario_id"],)
    )

    filas = cursor.fetchall()

    tareas_obj = []
    for fila in filas:
        tareas_obj.append(Tarea(fila[0], fila[1], fila[2]))

    cursor.close()
    conn.close()

    return render_template("tareas.html", tareas=tareas_obj)


@tareas_bp.route("/tareas/eliminar/<int:id>")
def eliminar_tarea(id):
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tareas WHERE id = %s AND usuario_id = %s",
        (id, session["usuario_id"])
    )
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("tareas.tareas"))


@tareas_bp.route("/api/tareas")
def api_tareas():
    if "usuario_id" not in session:
        return {"error": "No autorizado"}, 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, descripcion, usuario_id FROM tareas WHERE usuario_id = %s",
        (session["usuario_id"],)
    )

    filas = cursor.fetchall()
    tareas = [Tarea(f[0], f[1], f[2]) for f in filas]

    cursor.close()
    conn.close()

    return jsonify([t.to_dict() for t in tareas])
