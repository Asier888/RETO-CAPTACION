from flask import Flask, request, jsonify
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)

# Conexión a MySQL usando variables de entorno
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "db"),
    user=os.getenv("MYSQL_USER", "user"),
    password=os.getenv("MYSQL_PASSWORD", "pass"),
    database=os.getenv("MYSQL_DATABASE", "datos")
)

cursor = db.cursor()

@app.route("/datos", methods=["POST"])
def insertar_datos():
    data = request.json

    query = """
        INSERT INTO datos
        (timestamp, id_maquina, temperatura, presion, vibracion, humedad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        datetime.fromisoformat(data["timestamp"]),
        data["id_maquina"],
        data["temperatura"],
        data["presion"],
        data["vibracion"],
        data["humedad"]
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({"status": "dato insertado correctamente"}), 201


@app.route("/datos", methods=["GET"])
def obtener_datos():
    cursor.execute("SELECT * FROM datos")
    rows = cursor.fetchall()

    columnas = [
        "id",
        "timestamp",
        "id_maquina",
        "temperatura",
        "presion",
        "vibracion",
        "humedad"
    ]

    resultado = [dict(zip(columnas, fila)) for fila in rows]
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

