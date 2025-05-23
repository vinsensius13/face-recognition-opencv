# Face Recognition System using OpenCV

Proyek ini adalah sistem pengenalan wajah berbasis Python menggunakan OpenCV, yang terdiri dari tiga tahap utama:
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
├── requirements.txt
└── README.md

````

## 🔧 Instalasi

1. Clone repositori ini:

```bash
git clone https://github.com/username/face-recognition-opencv.git
cd face-recognition-opencv
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Pastikan file `haarcascade_frontalface_default.xml` berada di direktori yang sama dengan script, atau unduh dari [OpenCV GitHub](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

## 🚀 Cara Menjalankan

### 1. Capture Wajah

Jalankan:

```bash
python 01_face_dataset.py
```

* Masukkan **nama** dan **ID** pengguna.
* Sistem akan mengambil 30 gambar wajah dan menyimpannya ke folder `dataset/`.

### 2. Latih Model

Jalankan:

```bash
python 02_face_training.py 
```

* Model LBPH akan dilatih menggunakan gambar di `dataset/` dan disimpan ke `trainer/trainer.yml`.

### 3. Pengenalan Wajah

Jalankan:

```bash
python 02_face_recognition.py
```

* Sistem akan menampilkan kamera dan mengenali wajah secara realtime.
* Nama dan confidence level akan ditampilkan jika wajah dikenali.

## 🧠 Teknologi yang Digunakan

* Python 
* OpenCV (`opencv-contrib-python`)
* NumPy
* Pillow

