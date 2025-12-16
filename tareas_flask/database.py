import mysql.connector
from tareas_flask.config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
