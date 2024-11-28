import cv2
import os
import sys

# Recebe o nome da pessoa
person_name = sys.argv[1]  


# Cria o diretório para armazenar as imagens
os.makedirs(f'dataset/{person_name}', exist_ok=True)

# Inicia a captura de vídeo
cap = cv2.VideoCapture(0)

# Carrega o classificador de face
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img_id = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta faces no frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Salva cada face detectada
    for (x, y, w, h) in faces:
        img_id += 1
        face_img = gray[y:y+h, x:x+w]
        cv2.imwrite(f'dataset/{person_name}/face_{img_id}.jpg', face_img)

        # Desenha um retângulo ao redor da face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Capturando Faces', frame)

    # Encerra a captura após coletar 100 imagens ou se 'q' for pressionado
    if cv2.waitKey(1) & 0xFF == ord('q') or img_id >= 100:
        break

cap.release()
cv2.destroyAllWindows()
