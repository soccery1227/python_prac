import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load known faces
First_image = face_recognition.load_image_file("faces/1.jpeg")
First_encoding = face_recognition.face_encodings(First_image)[0]

Second_image = face_recognition.load_image_file("faces/2.jpeg")
Second_encoding = face_recognition.face_encodings(Second_image)[0]

known_face_encodings = [First_encoding, Second_encoding]
known_face_names = ["First", "Second"]

# List of expected students for attendance
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%d-%m-%y")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Add text if person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_PLAIN
            bottomleftCorner = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomleftCorner, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%Hh-%Mm-%Ss")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
