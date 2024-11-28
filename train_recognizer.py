import cv2
import numpy as np
import os

# Caminho para o dataset
dataset_path = 'dataset'

# Inicializa o reconhecedor facial
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Carrega o classificador de face
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Listas para armazenar as faces e labels
faces = []
labels = []

# Dicionário para mapear labels aos nomes
label_dict = {}
current_id = 0

# Percorre as pastas no dataset
for root, dirs, files in os.walk(dataset_path):
    for dir_name in dirs:
        label_dict[current_id] = dir_name
        subject_path = os.path.join(root, dir_name)

        for filename in os.listdir(subject_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(subject_path, filename)
                image = cv2.imread(image_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces_rect = face_cascade.detectMultiScale(gray, 1.1, 4)

                for (x, y, w, h) in faces_rect:
                    face = gray[y:y+h, x:x+w]
                    faces.append(face)
                    labels.append(current_id)
        current_id += 1

# Treina o reconhecedor com as faces e labels
recognizer.train(faces, np.array(labels))

# Salva o modelo treinado
recognizer.save('training_data.yml')

# Salva o dicionário de labels
np.save('labels.npy', label_dict)

print("Treinamento concluído. Modelo salvo como 'training_data.yml' e labels salvos como 'labels.npy'.")
