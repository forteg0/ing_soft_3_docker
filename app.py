import os
import logging
from urllib.parse import urlparse
from flask import Flask, jsonify
import mysql.connector

# Crear la app de Flask
app = Flask(__name__)

# -----------------------------
# Variables de entorno
# -----------------------------
APP_ENV = os.getenv("APP_ENV", "qa")  # "qa" o "production"
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql://default_user:default_pass@localhost:3306/default_db"
)

# -----------------------------
# Función para crear conexión a MySQL
# -----------------------------
def get_db_connection():
    try:
        db = urlparse(DATABASE_URL)
        conn = mysql.connector.connect(
            host=db.hostname,
            user=db.username,
            password=db.password,
            database=db.path[1:],  # quitar la barra inicial '/'
            port=db.port or 3306
        )
        return conn
    except mysql.connector.Error as err:
        raise

# -----------------------------
# Endpoints
# -----------------------------
@app.route("/users", methods=["GET"])
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(users=users), 200
    except Exception as e:
        return jsonify(error="Error al obtener usuarios"), 500

@app.route("/env", methods=["GET"])
def show_env():
    return jsonify(app_env=APP_ENV, database=DATABASE_URL), 200

@app.route("/config", methods=["GET"])
def config():
    return jsonify(database_url=DATABASE_URL), 200

# -----------------------------
# Ejecutar la app
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # debug=True para desarrollo
