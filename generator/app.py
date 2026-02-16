import time
import numpy as np
from datetime import datetime, timezone

ID_MAQUINA = "MAQUINA_01"

def generar_datos():
    # Timestamp en formato epoch millis
    timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)

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
        print(datos)
        time.sleep(5)
