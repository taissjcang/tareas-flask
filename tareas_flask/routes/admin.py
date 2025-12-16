from flask import Blueprint, render_template, redirect, url_for, request, session
from tareas_flask.database import get_connection

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


def es_admin():
    return session.get("es_admin") is True


@admin_bp.route("/usuarios")
def gestionar_usuarios():
    if not es_admin():
        return redirect(url_for("tareas.tareas"))

    busqueda = request.args.get("q", "").strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if busqueda:
        cursor.execute("""
            SELECT u.id, u.username, u.es_admin, u.creado_en,
                   COUNT(t.id) AS cantidad_tareas
            FROM usuarios u
            LEFT JOIN tareas t ON u.id = t.usuario_id
            WHERE u.id = %s OR u.username LIKE %s
            GROUP BY u.id
        """, (busqueda, f"%{busqueda}%"))
    else:
        cursor.execute("""
            SELECT u.id, u.username, u.es_admin, u.creado_en,
                   COUNT(t.id) AS cantidad_tareas
            FROM usuarios u
            LEFT JOIN tareas t ON u.id = t.usuario_id
            GROUP BY u.id
        """)

    usuarios = cursor.fetchall()
    conn.close()

    return render_template("admin_usuarios.html", usuarios=usuarios, busqueda=busqueda)


@admin_bp.route("/usuarios/eliminar/<int:id>")
def eliminar_usuario(id):
    if not es_admin():
        return redirect(url_for("tareas.tareas"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tareas WHERE usuario_id = %s", (id,))
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("admin.gestionar_usuarios"))


@admin_bp.route("/usuarios/promover/<int:id>")
def promover_usuario(id):
    if not es_admin():
        return redirect(url_for("tareas.tareas"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE usuarios SET es_admin = 1 WHERE id = %s", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("admin.gestionar_usuarios"))
