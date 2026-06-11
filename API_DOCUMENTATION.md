# Dokumentasi API - MediCare AI 🔌

Backend MediCare AI dibangun menggunakan **FastAPI**. Layanan ini bertugas menerima data klinis dari *client* (Frontend), meneruskannya ke AI Engine, dan mengembalikan hasil prediksi.

- **Base URL:** `http://54.179.236.97:8000`
- **Interactive Swagger UI:** `http://54.179.236.97:8000/docs`

## 1. Health Check
Endpoint untuk memastikan server Backend berjalan dengan normal.
- **URL:** `/`
- **Method:** `GET`
- **Success Response:**
  ```json
  {
    "message": "MediCare AI Backend is running gracefully"
  }

## 2. Prediksi Penyakit Jantung
Endpoint utama untuk memproses 13 parameter klinis pasien melalui model Machine Learning.

URL: /predict

Method: POST

Headers: Content-Type: application/json

Request Body (JSON):
{
  "age": 65,
  "sex": 1,
  "cp": 3,
  "trestbps": 160,
  "chol": 280,
  "fbs": 1,
  "restecg": 2,
  "thalach": 110,
  "exang": 1,
  "oldpeak": 2.5,
  "slope": 2,
  "ca": 3,
  "thal": 3
}

Success Response (JSON):
{
  "kode_hasil": 1,
  "status_prediksi": "Risiko Tinggi Penyakit Jantung"
}
