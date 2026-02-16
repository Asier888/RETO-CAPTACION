from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import time

# CONFIGURACIÓN
DB_HOST = "db"
DB_USER = "user"
DB_PASSWORD = "userpass"
DB_NAME = "datos"

#espera para que no conecte antes a mysql
def esperar_mysql():
    while True:
        try:
            connection = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            print("Conectado a MySQL")
            return connection
        except Error:
            print("MySQL no disponible, reintentando en 3s...")
            time.sleep(3)


db = esperar_mysql()
cursor = db.cursor()

app = Flask(__name__)

@app.route("/datos", methods=["POST"])
def recibir_datos():
    data = request.json

    try:
        cursor.execute(
            """
            INSERT INTO datos 
            (timestamp, id_maquina, temperatura, presion, vibracion, humedad)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                data["timestamp"],
                data["id_maquina"],
                data["temperatura"],
                data["presion"],
                data["vibracion"],
                data["humedad"]
            )
        )
        db.commit()
        return jsonify({"status": "dato insertado correctamente"}), 201

    except Exception as e:
        print("Error insertando datos:", e)
        return jsonify({"error": "error insertando datos"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
