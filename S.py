import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime, timedelta
import pandas as pd

# Ensure the path exists
path = 'ImagesAttendance'
if not os.path.exists(path):
    os.makedirs(path)

# Load images and class names
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    if cl != '.DS_Store':
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
print(classNames)

# Function to find encodings
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if len(encode) > 0:
            encodeList.append(encode[0])
    return encodeList

# Function to mark attendance
def markAttendance(name):
    file_exists = os.path.isfile('Attendance.csv')
    if not file_exists:
        df = pd.DataFrame(columns=['Name', 'Time'])
        df.to_csv('Attendance.csv', index=False)
    else:
        df = pd.read_csv('Attendance.csv')
    
    nameList = df['Name'].tolist()
    if name not in nameList:
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')

        if len(df) > 0:
            last_entry_time = datetime.strptime(df.iloc[-1]['Time'], '%H:%M:%S')
            time_diff = now - last_entry_time
            if time_diff > timedelta(hours=1):
                new_entry = pd.DataFrame({'Name': [name], 'Time': [dtString]})
                df = pd.concat([df, new_entry], ignore_index=True)
        else:
            new_entry = pd.DataFrame({'Name': [name], 'Time': [dtString]})
            df = pd.concat([df, new_entry], ignore_index=True)
            
        df.to_csv('Attendance.csv', index=False)

# Encode known faces
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
