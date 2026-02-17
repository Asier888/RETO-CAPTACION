import time
import numpy as np
import requests
from datetime import datetime, timezone

ID_MAQUINA = "M01"
API_URL = "http://api:8000/datos"  # nombre del servicio en docker-compose

def generar_datos():
    timestamp = datetime.now(timezone.utc).isoformat()

    datos = {
        "timestamp": timestamp,
        "id_maquina": ID_MAQUINA,
        "temperatura": round(60 + np.random.normal(0, 2), 2),
        "presion": round(30 + np.random.normal(0, 1), 2),
        "vibracion": round(5 + np.random.normal(0, 0.5), 2),
        "humedad": round(40 + np.random.normal(0, 3), 2)
    }

    return datos


if __name__ == "__main__":
    print("Iniciando generador de datos...\n")

    while True:
        datos = generar_datos()

        try:
            response = requests.post(API_URL, json=datos)
            print(f"Enviado: {datos} | Status: {response.status_code}")
        except Exception as e:
            print(f"Error enviando datos: {e}")

        time.sleep(5)
