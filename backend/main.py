from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

# Inisialisasi Aplikasi FastAPI
app = FastAPI(title="API Prediksi Penyakit Jantung", description="Backend AI Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Mengizinkan web dari mana saja untuk mengakses API ini
    allow_credentials=True,
    allow_methods=["*"],  # Mengizinkan semua metode (termasuk POST dan OPTIONS)
    allow_headers=["*"],
)


# Muat Model dan Objek Preprocessing
model = joblib.load('rf_heart_model.pkl')
scaler = joblib.load('scaler_heart.pkl')
pca = joblib.load('pca_heart.pkl')

# Kontrak Data (Skema Input dari Frontend)
class DataPasien(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

@app.get("/")
def read_root():
    return {"message": "AI Service Aktif. Akses /docs untuk dokumentasi API."}

@app.post("/predict")
def prediksi_risiko(data: DataPasien):
    # 1. Konversi input JSON ke DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # 2. Normalisasi Z-Score (sesuai saat training)
    scaled_data = scaler.transform(input_df)
    
    # 3. Reduksi Dimensi dengan PCA
    pca_data = pca.transform(scaled_data)
    
    # 4. Prediksi menggunakan Random Forest
    prediksi = model.predict(pca_data)
    
    # 5. Format Hasil Output
    status = "Risiko Tinggi Penyakit Jantung" if prediksi[0] == 1 else "Risiko Rendah (Sehat)"
    
    return {
        "status_prediksi": status,
        "kode_hasil": int(prediksi[0])
    }