import cv2
import numpy as np

# Carrega o classificador de face
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carrega o reconhecedor facial treinado
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training_data.yml')

# Carrega o dicionário de labels
label_dict = np.load('labels.npy', allow_pickle=True).item()

# Inicializa a captura de vídeo
video_capture = cv2.VideoCapture(0)

while True:
    # Lê o frame atual
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Reconhece a face
        label, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Verifica a confiança
        if confidence < 100:
            name = label_dict[label]
            confidence_text = f"{round(100 - confidence)}%"
        else:
            name = "Desconhecido"
            confidence_text = f"{round(100 - confidence)}%"

        # Desenha o retângulo e exibe o nome
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({confidence_text})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Exibe o frame
    cv2.imshow('Reconhecimento Facial', frame)

    # Encerra se 'q' for pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha as janelas
video_capture.release()
cv2.destroyAllWindows()
