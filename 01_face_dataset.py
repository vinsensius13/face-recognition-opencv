import cv2
import os
import re

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
directory = 'dataset/'
face_name = input('\n enter user name end press <return> ==>  ')
face_id = input("\n enter your Id= ")

# Inisialisasi nilai id maksimum
#max_id = 0

# Loop melalui setiap file di direktori
for filename in os.listdir(directory):
    # Cek jika nama file adalah file gambar dengan ekstensi .jpg
    if filename.endswith('.jpg'):
        # Gunakan ekspresi reguler untuk mengekstrak id dari nama file
        match = re.match(r'(\w+)\.(\d+)\.\d+\.jpg', filename)
        if match:
            # Ambil nilai id dari hasil pencocokan
            file_id = int(match.group(2))
            # Perbarui nilai id maksimum jika diperlukan
            #max_id = max(max_id, file_id)


#face_id = max_id + 1
#print("FACE ID: ", face_id)

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        
        # Save the captured image into the datasets folder
        cv2.imwrite(str(directory) + str(face_name) +"." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()