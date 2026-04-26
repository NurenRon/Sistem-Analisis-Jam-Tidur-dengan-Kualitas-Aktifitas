# Sistem Penentuan Jam Tidur Sehat (AI Sleep Analysis)

Sistem Penentuan Jam Tidur Sehat adalah sebuah aplikasi berbasis web yang memanfaatkan Kecerdasan Buatan (AI) untuk menganalisis dan merekomendasikan durasi serta pola tidur terbaik bagi mahasiswa. Sistem ini menggabungkan dua metode AI, yaitu **Sistem Pakar (Rule-Based)** dan **Logika Fuzzy**, dengan antarmuka pengguna (UI) modern bergaya *Glassmorphism*.

---

## Fitur Utama

1. **Sistem Pakar (Forward Chaining)**
   - Menggunakan 15 pertanyaan interaktif berbasis *Rule-Based Forward Chaining*.
   - Menganalisis kebiasaan harian, rutinitas, dan kondisi fisik mahasiswa.
   - Menghasilkan 5 kategori diagnosis spesifik (Misal: *Kurang Tidur Kronis*, *Early Bird Terstruktur*).
2. **Sistem Logika Fuzzy (Mamdani)**
   - Menganalisis parameter intensitas harian: Tingkat Kelelahan Fisik, Stres Mental, dan Pengganggu Tidur (Skala 0-100).
   - Menghitung durasi tidur presisi menggunakan kurva keanggotaan (*Membership Function*).
   - Menghasilkan visualisasi grafik defuzzifikasi secara *real-time*.
3. **Modern & Responsive UI/UX**
   - Dibangun menggunakan Bootstrap 5 dan CSS Kustom.
   - Mengusung tema *Glassmorphism* (efek kaca) dan gradien warna yang menenangkan.

---

## Teknologi yang Digunakan

* **Backend:** Python 3, Flask
* **AI Engine:** `scikit-fuzzy` (Logika Fuzzy), Custom Python Dictionary (Sistem Pakar)
* **Data Visualization:** `matplotlib`, `numpy`
* **Frontend:** HTML5, CSS3, Bootstrap 5, Font Poppins

---

## Struktur Direktori

```text
SistemTidurSehat/
│
├── app.py                 # File utama aplikasi (Routing Flask & Mesin AI)
├── README.md              # Dokumentasi proyek
└── templates/             # Folder wajib Flask untuk file HTML
    ├── index.html         # Halaman utama (Pemilihan sistem)
    ├── pakar.html         # Antarmuka kuis Sistem Pakar
    └── fuzzy.html         # Antarmuka slider Logika Fuzzy