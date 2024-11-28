import tensorflow as tf
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Diretório do dataset
dataset_path = 'dataset'

# Carregar as imagens e labels
data = []
labels = []

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith('.jpg'):
            img_path = os.path.join(root, file)
            image = tf.keras.preprocessing.image.load_img(img_path, target_size=(160, 160))
            image = tf.keras.preprocessing.image.img_to_array(image) / 255.0
            label = os.path.basename(root)
            data.append(image)
            labels.append(label)

data = np.array(data)
labels = np.array(labels)

# Codificação de labels
encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)
labels_dict = dict(zip(encoder.classes_, range(len(encoder.classes_))))

# Divisão em treino e validação
X_train, X_test, y_train, y_test = train_test_split(data, encoded_labels, test_size=0.2, random_state=42)

# Modelo pré-treinado
base_model = tf.keras.applications.MobileNetV2(input_shape=(160, 160, 3), include_top=False, weights='imagenet')
base_model.trainable = False

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(len(labels_dict), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10)

# Salvar modelo e labels
model.save('facial_recognition_model.h5')
np.save('labels.npy', labels_dict)
print("Treinamento concluído.")
