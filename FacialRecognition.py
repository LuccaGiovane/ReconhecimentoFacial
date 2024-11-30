import cv2
import tensorflow as tf
import numpy as np

# Carregar modelos e labels
face_model = tf.keras.models.load_model('facial_recognition_model.h5')
emotion_model = tf.keras.models.load_model('emotion_recognition_model.keras')

# Carregar labels de reconhecimento facial
labels_dict = np.load('labels.npy', allow_pickle=True).item()
reverse_labels_dict = {v: k for k, v in labels_dict.items()}

# Definir classes de emoções
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Configurar vídeo e detecção
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        
        # Reconhecimento facial
        face_resized = cv2.resize(face, (160, 160)) / 255.0
        face_resized = np.expand_dims(face_resized, axis=0)
        predictions = face_model.predict(face_resized)
        label = np.argmax(predictions)
        name = reverse_labels_dict.get(label, "Desconhecido")
        confidence = round(np.max(predictions) * 100, 2)
        
        # Detecção de emoção
        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        face_gray_resized = cv2.resize(face_gray, (48, 48)) / 255.0
        face_gray_resized = np.expand_dims(face_gray_resized, axis=0)
        face_gray_resized = np.expand_dims(face_gray_resized, axis=-1)
        emotion_predictions = emotion_model.predict(face_gray_resized)
        emotion_label = emotion_labels[np.argmax(emotion_predictions)]
        emotion_confidence = round(np.max(emotion_predictions) * 100, 2)
        
        # Desenhar retângulo e textos
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({confidence}%)", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, f"Emocao: {emotion_label} ({emotion_confidence}%)", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow('Reconhecimento Facial e Emocional', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
