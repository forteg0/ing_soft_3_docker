FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer el puerto de Flask
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]
