import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

# Inisialisasi dictionary untuk menyimpan id dan nama
id_names = {}

# Mendapatkan daftar file dalam direktori dataset
dataset_dir = 'dataset/'
files = os.listdir(dataset_dir)

# Memproses setiap file dalam direktori dataset
for file in files:
    if file.endswith('.jpg'):
        # Membagi nama file untuk mendapatkan id
        parts = file.split('.')
        id = int(parts[1])  # Mengambil id dari nama file
        name = parts[0]     # Mengambil nama dari nama file (tanpa id), boleh diimprove kalau mau lebih akurat

        # Menambahkan id dan nama ke dalam dictionary (kalau id belum pernah masuk)
        if id not in id_names:
            id_names[id] = name

# Membuat array names berdasarkan id_names, aman supaya ga KeyError
if len(id_names) > 0:
    max_id = max(id_names.keys())
    names = ['None'] + [id_names.get(i, 'Unknown') for i in range(1, max_id + 1)]
else:
    names = ['None']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        id_predicted, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Cek apakah id valid di names
        if confidence < 100:
            if id_predicted < len(names):
                display_name = names[id_predicted]
            else:
                display_name = "unknown"
            confidence_text = "  {0}%".format(round(100 - confidence))
        else:
            display_name = "unknown"
            confidence_text = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(display_name), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence_text), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
