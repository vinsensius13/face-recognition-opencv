# Face Recognition System using OpenCV

Proyek ini adalah sistem **Pengenalan Wajah** berbasis **Python** menggunakan **OpenCV**, yang terdiri dari tiga tahap utama:

1. **Pengambilan Gambar Wajah**
2. **Pelatihan Model**
3. **Pengenalan Wajah secara Realtime**

## 📁 Struktur Folder

```
.
├── dataset/                # Menyimpan gambar wajah yang di-capture
├── trainer/                # Menyimpan model hasil pelatihan
├── haarcascade_frontalface_default.xml
├── 01_face_dataset.py      # Script untuk capture wajah
├── 02_face_training.py     # Script untuk melatih model
├── 03_face_recognition.py  # Script untuk pengenalan wajah
├── requirements.txt        # Daftar dependencies
└── README.md
```

## 🔧 Instalasi & Persiapan

1. **Clone repositori ke GitHub pribadi / lokal:**

```bash
git clone https://github.com/vinsensius13/face-recognition-opencv.git
cd face-recognition-opencv
```

2. **Buat virtual environment (optional tapi disarankan):**

```bash
python -m venv .venv
& ".venv\Scripts\Activate.ps1"  # Windows (PowerShell)
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Pastikan file `haarcascade_frontalface_default.xml` tersedia di direktori utama**, atau bisa diunduh dari:
   👉 [OpenCV GitHub - Haarcascade](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

---

## 🚀 Cara Penggunaan

### 1️⃣ **Capture Wajah**

```bash
python 01_face_dataset.py
```

* Masukkan **nama pengguna** dan **ID (angka)**.
* Sistem akan mengambil ±30 gambar wajah.
* Gambar akan disimpan di folder `dataset/`.

### 2️⃣ **Latih Model**

```bash
python 02_face_training.py
```

* Sistem akan melatih model pengenalan wajah menggunakan gambar dari `dataset/`.
* Model akan disimpan di folder `trainer/trainer.yml`.

### 3️⃣ **Pengenalan Wajah (Realtime)**

```bash
python 03_face_recognition.py
```

* Sistem akan membuka webcam.
* Wajah yang dikenal akan ditampilkan dengan **nama** + **confidence score**.
* Tekan `ESC` untuk keluar dari aplikasi.

---

## 🧠 Teknologi yang Digunakan

* **Python 3.x**
* **OpenCV** (`opencv-contrib-python`)
* **NumPy**
* **Pillow** (opsional untuk pengolahan gambar)

---

## ℹ️ Catatan

* Proyek ini bertujuan sebagai **implementasi dasar Face Recognition**.
* Model yang digunakan: **LBPH (Local Binary Pattern Histogram)** → cocok untuk sistem ringan.
* Untuk produksi / akurasi tinggi, dapat menggunakan model berbasis Deep Learning.

---

Selamat mencoba! 🚀

---

[Repo by Vinsensius13 - GitHub](https://github.com/vinsensius13/face-recognition-opencv.git)

---

---

*Project for Mini Assignment - Face Recognition System using OpenCV*
