# Sleep Analysis — Sistem Penentuan Jam Tidur Sehat

> Sistem berbasis web **Pure Frontend** untuk menganalisis dan merekomendasikan pola tidur terbaik bagi mahasiswa — menggunakan dua metode AI: **Sistem Pakar (Forward Chaining)** dan **Logika Fuzzy (Mamdani)**.

---

## Tentang Proyek

**Sleep Analysis** adalah konversi penuh dari proyek berbasis Flask menjadi **satu file HTML statis** yang dapat dijalankan langsung di browser tanpa server, tanpa Python, dan tanpa instalasi apapun.

Semua logika yang sebelumnya berjalan di backend Python — termasuk mesin inferensi sistem pakar dan kalkulasi fuzzy — telah diimplementasi ulang sepenuhnya menggunakan **JavaScript murni**.

---

## Fitur Utama

### 1. Sistem Pakar (Forward Chaining)
- **15 pertanyaan interaktif** dengan jawaban Ya / Tidak
- Analisis kebiasaan harian, kondisi fisik, dan rutinitas mahasiswa
- Mesin inferensi berbasis **skor kemiripan** terhadap 5 aturan kesimpulan
- Menghasilkan **6 kategori diagnosis** beserta rekomendasi jam tidur spesifik

| Kesimpulan | Rekomendasi |
|---|---|
| Pola Tidur Ideal | 22.00 – 06.00 (8 Jam) |
| Early Bird Terstruktur | 21.30 – 05.30 (8 Jam) |
| Night Owl Terkendali | 00.00 – 07.00 (7 Jam) |
| Kurang Tidur Kronis | 23.00 – 06.00 + Power Nap |
| Gangguan Pola Tidur | 22.00 – 06.00 + Perubahan Kebiasaan |
| Pola Tidur Campuran | 22.30 – 06.00 (7.5 Jam) |

### 2. Logika Fuzzy (Mamdani)
- Input berupa **3 slider** (skala 0–100):
  - Kelelahan Fisik
  - Stres / Beban Mental
  - Pengganggu Tidur (Kafein / Screen Time)
- Implementasi manual fungsi keanggotaan: `trapmf` dan `trimf`
- **4 aturan Mamdani** yang diterapkan secara agregasi
- **Defuzzifikasi Centroid** untuk menghasilkan nilai durasi tidur presisi
- Visualisasi **grafik kurva fuzzy** interaktif (Kurang / Ideal / Ekstra + Agregasi)
- **9 membership card** yang menampilkan derajat keanggotaan per input secara real-time

### 3. UI / UX Modern
- Desain **Glassmorphism** dengan efek kaca dan ambient glow
- Font **DM Serif Display + DM Sans** untuk estetika yang bersih dan modern
- **Animasi transisi** pertanyaan dan progress bar
- Fully **responsive** untuk berbagai ukuran layar
- Navigasi antar halaman tanpa reload (Single Page Application)

---

## Teknologi yang Digunakan

| Kategori | Teknologi |
|---|---|
| Struktur | HTML5 |
| Tampilan | CSS3, Glassmorphism, Custom Properties |
| Logika AI | JavaScript (Vanilla) |
| Visualisasi | Chart.js 4.4.1 (via CDN) |
| Tipografi | Google Fonts — DM Serif Display, DM Sans |

> ⚠️ **Tidak ada backend, tidak ada framework, tidak ada instalasi.**

---

## 📁 Struktur Proyek

```
sleep-analysis/
│
├── sistem_tidur.html     # Seluruh aplikasi dalam satu file
└── README.md             # Dokumentasi ini
```

Berbeda dengan versi Flask yang membutuhkan beberapa file dan server, versi ini merangkum **seluruh aplikasi** — halaman index, sistem pakar, logika fuzzy, styling, dan logika AI — ke dalam **satu file HTML tunggal**.

---

## Cara Menjalankan

Karena ini adalah pure frontend, cara menjalankannya sangat sederhana:

### Buka Langsung di Browser
```bash
# Klik dua kali file-nya, atau:
open sistem_tidur.html        # macOS
start sistem_tidur.html       # Windows
xdg-open sistem_tidur.html    # Linux
```

### ▶ Jalankan via Live Server (Opsional)
Jika menggunakan VS Code, kamu bisa klik kanan pada file → **Open with Live Server**.

> ✅ Tidak perlu `pip install`, tidak perlu `flask run`, tidak perlu Python.

---

## 🔄 Perbandingan: Versi Flask vs Versi Pure Frontend

| Aspek | Versi Flask (Lama) | Versi Pure Frontend (Baru) |
|---|---|---|
| Menjalankan aplikasi | `flask run` + Python | Klik file HTML |
| Dependensi | Flask, scikit-fuzzy, matplotlib, numpy | Tidak ada |
| Jumlah file | 4+ file (app.py + 3 template) | **1 file** |
| Logika Fuzzy | scikit-fuzzy + matplotlib | JavaScript + Chart.js |
| Grafik Defuzzifikasi | Gambar PNG base64 (statis) | Canvas interaktif (dinamis) |
| Deployment | Butuh server Python | Bisa di GitHub Pages, Netlify, dll |
| Offline | ❌ | ✅ (jika Chart.js di-cache) |

---

## 🧩 Cara Kerja Sistem

### Sistem Pakar
```
User menjawab 15 pertanyaan (Ya/Tidak)
        ↓
Setiap jawaban disimpan sebagai { P1: 'y', P2: 't', ... }
        ↓
Dibandingkan dengan syarat 5 aturan kesimpulan
        ↓
Kesimpulan dengan skor kemiripan tertinggi dipilih
        ↓
Hasil + rekomendasi jam tidur ditampilkan
```

### Logika Fuzzy
```
User input nilai Fisik, Mental, Pengganggu (0–100)
        ↓
Hitung derajat keanggotaan tiap himpunan (trapmf / trimf)
        ↓
Terapkan 4 aturan Mamdani → firing strength per output
        ↓
Agregasi kurva output (MAX dari clipped MF)
        ↓
Defuzzifikasi Centroid → nilai jam tidur presisi
        ↓
Grafik + status ditampilkan
```

---

## Target Pengguna

Sistem ini dirancang khusus untuk **mahasiswa** dengan berbagai pola aktivitas:
- Mahasiswa dengan jadwal kuliah pagi
- Mahasiswa yang aktif berorganisasi malam hari
- Mahasiswa yang sering begadang mengerjakan tugas
- Mahasiswa dengan beban akademik tinggi

---

## Referensi Ilmiah

- National Sleep Foundation merekomendasikan **7–9 jam** tidur per malam untuk dewasa muda (18–25 tahun)
- Kurang tidur kronis (<6 jam) berhubungan dengan penurunan fungsi kognitif, memori, dan konsentrasi
- Penggunaan layar digital sebelum tidur menghambat produksi **melatonin**
- Konsistensi *sleep schedule* lebih berpengaruh terhadap kualitas tidur dibanding durasi semata

---

## Lisensi

Proyek ini dibuat untuk keperluan akademik. Bebas digunakan dan dimodifikasi dengan menyertakan atribusi.