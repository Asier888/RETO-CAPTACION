#versión ligera de una imagen basada en python
FROM python:3.11-slim

# crear carpeta app de trabajo dentro del contenedor
WORKDIR /app

# copia dependencias al contenedor
COPY requirements.txt .

# instalar las dependencia
# "--no-cache-dir" buena práctica en docker para no guardar cache
# y hacer la imagen más pequeña, evitando archivos innecesarios
RUN pip install --no-cache-dir -r requirements.txt

# copiar código de guardado en base de datos
COPY api.py .

# ejecutar programa
CMD ["python", "api.py"]
