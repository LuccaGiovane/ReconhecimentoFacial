import cv2
import tensorflow as tf
import numpy as np

# Carregar modelo e labels
model = tf.keras.models.load_model('facial_recognition_model.h5')
labels_dict = np.load('labels.npy', allow_pickle=True).item()
reverse_labels_dict = {v: k for k, v in labels_dict.items()}

# Configurar vídeo e detecção
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (160, 160)) / 255.0
        face_resized = np.expand_dims(face_resized, axis=0)
        
        predictions = model.predict(face_resized)
        label = np.argmax(predictions)
        name = reverse_labels_dict[label]
        confidence = round(np.max(predictions) * 100, 2)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({confidence}%)", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('Reconhecimento Facial', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
