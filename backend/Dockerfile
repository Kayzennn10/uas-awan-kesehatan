# Gunakan image Python yang ringan
FROM python:3.10-slim

# Set direktori kerja di dalam kontainer
WORKDIR /app

# Salin requirements dan install library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode backend dan model AI kamu
COPY . .

# Ekspos port 8000
EXPOSE 8000

# Perintah untuk menjalankan server FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]