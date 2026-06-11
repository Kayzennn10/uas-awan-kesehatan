-- Skema Database untuk Sistem Prediksi Penyakit Jantung
-- Tabel ini digunakan untuk menyimpan riwayat pengecekan indikator kesehatan pasien

CREATE TABLE riwayat_prediksi (
    id_pasien INT AUTO_INCREMENT PRIMARY KEY,
    waktu_cek TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    age FLOAT NOT NULL,
    sex FLOAT NOT NULL,
    cp FLOAT NOT NULL,
    trestbps FLOAT NOT NULL,
    chol FLOAT NOT NULL,
    fbs FLOAT NOT NULL,
    restecg FLOAT NOT NULL,
    thalach FLOAT NOT NULL,
    exang FLOAT NOT NULL,
    oldpeak FLOAT NOT NULL,
    slope FLOAT NOT NULL,
    ca FLOAT NOT NULL,
    thal FLOAT NOT NULL,
    status_prediksi VARCHAR(50) NOT NULL,
    kode_hasil INT NOT NULL
);

-- Contoh Insert Data (Dummy Data untuk Testing)
INSERT INTO riwayat_prediksi (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, status_prediksi, kode_hasil) 
VALUES (45, 1, 3, 110, 264, 0, 1, 132, 0, 1.2, 1, 0, 2, 'Risiko Tinggi Penyakit Jantung', 1);