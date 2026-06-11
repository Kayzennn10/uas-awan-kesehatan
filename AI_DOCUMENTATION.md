# Dokumentasi AI Engine - MediCare AI 🧠

Aplikasi ini menggunakan model **Machine Learning** khusus (dikemas dalam format `.pkl`) yang dilatih untuk mendeteksi pola indikasi penyakit jantung dari rekam medis dasar pasien.

## ⚙️ Spesifikasi Model
- **Jenis AI:** Machine Learning Classification
- **Library Utama:** Scikit-Learn, Pandas, NumPy
- **Format Model:** Pickle / Joblib Serialization (`.pkl`)
- **Deployment:** Di-*load* ke dalam memori oleh Uvicorn (FastAPI) saat server pertama kali menyala (Cold Start optimization).

## 📊 Parameter Input (Features)
Model membutuhkan 13 *features* klinis berformat numerik (`float` atau `int`) untuk menghasilkan prediksi:
1. `age`: Umur pasien (tahun).
2. `sex`: Jenis kelamin (1 = Pria, 0 = Wanita).
3. `cp`: Tipe nyeri dada (0-3).
4. `trestbps`: Tekanan darah saat istirahat (mmHg).
5. `chol`: Kolesterol serum (mg/dl).
6. `fbs`: Gula darah puasa (> 120 mg/dl = 1, else = 0).
7. `restecg`: Hasil elektrokardiografi istirahat (0-2).
8. `thalach`: Detak jantung maksimum yang dicapai.
9. `exang`: Angina akibat olahraga (1 = Ya, 0 = Tidak).
10. `oldpeak`: Depresi ST yang diinduksi oleh olahraga.
11. `slope`: Kemiringan segmen ST latihan puncak (0-2).
12. `ca`: Jumlah pembuluh darah utama (0-4).
13. `thal`: Indikator Thalassemia (0-3).

## 🎯 Output / Klasifikasi
Model akan mengklasifikasikan data ke dalam dua label probabilitas:
- **`[0]` (Negatif):** Indikator jantung pasien normal (Low Risk).
- **`[1]` (Positif):** Terdapat pola kuat indikasi penyakit jantung (High Risk).
