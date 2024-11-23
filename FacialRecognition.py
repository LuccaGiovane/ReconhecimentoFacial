import cv2
import os

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the training data
recognizer.read('training_data.yml')

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

while True:

    # Read the current frame from the video capture
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over each detected face
    for (x, y, w, h) in faces:

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Recognize the face
        label, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Display the name of the recognized person
        if confidence < 100:
            name = "Person " + str(label)
        else:
            name = "Unknown"

        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Recognizer', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()