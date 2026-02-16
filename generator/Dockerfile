FROM python:3.11-slim

WORKDIR /app

# copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copiar código y ejecutarlo
COPY app.py .
CMD ["python", "app.py"]
