from flask import Blueprint, session, jsonify
from tareas_flask.database import get_connection

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/tareas", methods=["GET"])
def api_tareas():
    # Verificar si el usuario está logueado
    if "usuario_id" not in session:
        return jsonify({"error": "No autorizado"}), 401

    usuario_id = session["usuario_id"]

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, descripcion FROM tareas WHERE usuario_id = %s",
        (usuario_id,)
    )

    tareas = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(tareas)
