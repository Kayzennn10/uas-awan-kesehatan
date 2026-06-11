# MediCare AI - Cloud Native Health Screening 🏥

MediCare AI adalah aplikasi skrining risiko penyakit jantung berbasis *Artificial Intelligence* (Machine Learning). Proyek ini dikembangkan untuk memenuhi Evaluasi Akhir Semester (EAS) mata kuliah Cloud Computing, dengan berfokus pada **Sustainable Development Goals (SDGs) Poin 3: Good Health and Well-being**.

## ☁️ Arsitektur Cloud & Teknologi
Aplikasi ini mengadopsi **Cloud Native Architecture** dan **Multi-Cloud Architecture**:
- **Compute Engine:** AWS EC2 (Ubuntu)
- **Object Storage & CDN:** Cloudinary (Multi-Cloud implementation)
- **Frontend:** HTML5, TailwindCSS, Vanilla JS
- **Backend / API:** FastAPI (Python)
- **AI Service:** Scikit-Learn (Machine Learning)
- **Containerization:** Docker & Docker Compose
- **CI/CD Pipeline:** GitHub Actions

## 📂 Struktur Repository
- `/frontend` : Berisi antarmuka web (UI/UX) untuk input pasien.
- `/backend` : Berisi logika API FastAPI dan model AI (`.pkl`).
- `database.sql` : Skema database proyek.
- `docker-compose.yml` : Konfigurasi orkestrasi container.
- `deploy.yml` (di `.github/workflows`) : Pipeline CI/CD otomatisasi ke AWS.

## 🚀 CI/CD Pipeline Workflow
Setiap kali ada perubahan kode yang di-*push* ke branch `main`, GitHub Actions akan otomatis menjalankan:
1. **Build & Test:** Memastikan tidak ada error pada kode.
2. **Dockerize:** Membangun *image* Docker untuk Frontend dan Backend.
3. **Push to Registry:** Mengirim *image* ke Docker Hub.
4. **Deploy to AWS:** Melakukan SSH ke EC2, menarik *image* terbaru, dan menjalankan `docker-compose up -d`.

## 👥 Anggota Kelompok
- Rifki (Frontend & CI/CD)
- [Nama Kamu] (Cloud Architecture & Backend)
- [Nama Anggota 3 jika ada] (AI Service)

---
*Dibuat untuk Tugas Cloud Computing - Institut Teknologi Nasional (Itenas) 2026*
