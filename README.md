# FaceTrack-Attendance-System

Project Description: FaceTrack Attendance System

Introduction
The FaceTrack Attendance System is an innovative project that leverages facial recognition technology to automate and streamline the process of attendance tracking. It uses real-time video capture to detect and recognize faces, subsequently logging attendance data into a CSV file. This project significantly reduces the manual effort required for attendance management and improves accuracy.

Project Components
Image Preprocessing and Encoding:

Image Collection: The system collects images from a specified directory (ImagesAttendance). Each image corresponds to an individual whose attendance will be tracked.
Image Loading and Name Extraction: Images are loaded into a list, and their corresponding class names (derived from the image file names) are extracted and stored in another list.
Face Encoding: Each loaded image is converted from BGR to RGB format. The face_recognition library is used to generate facial encodings for each image. These encodings serve as unique identifiers for each individual and are stored in a list for later comparison.
Real-Time Face Recognition:

Webcam Initialization: The system initializes the webcam to capture a real-time video feed.
Frame Processing: Each frame captured from the webcam is resized for faster processing and converted from BGR to RGB format.
Face Detection and Encoding: The system detects faces in the current frame and generates encodings for each detected face.
Face Matching: The encodings of detected faces are compared against the stored encodings of known faces. If a match is found (based on a distance threshold), the corresponding name is retrieved.
Attendance Marking:

CSV File Handling: The system checks if the Attendance.csv file exists. If not, it creates the file with the appropriate columns (Name and Time).
Name Checking and Time Logging: The system reads the existing attendance data and checks if the detected name is already logged. If the name is not found or if the last entry was more than an hour ago, the current time is recorded and added to the CSV file.
Updating the CSV File: The new attendance record is appended to the existing CSV file, ensuring that each entry is unique and logged only once per hour.
Visual Feedback:

Drawing Bounding Boxes: For each recognized face, a bounding box is drawn around the face in the webcam feed.
Displaying Names: The name of the recognized individual is displayed below the bounding box, providing immediate visual feedback and confirming the recognition process.
Workflow
Setup and Initialization: The necessary libraries are imported, and the path to the images directory is checked and created if it doesn't exist.

Loading Images and Encoding Faces: The system loads images from the specified directory, extracts class names, converts images to RGB format, and generates facial encodings for each image.

Real-Time Face Recognition and Attendance Marking:

The webcam captures a real-time video feed, and each frame is processed to detect and encode faces.
The detected faces are matched against the stored encodings of known faces.
If a match is found, the corresponding name is displayed, and attendance is marked by logging the name and time into a CSV file.
User Interaction: The system provides real-time visual feedback by displaying the recognized names and bounding boxes around detected faces in the webcam feed.

Conclusion
The FaceTrack Attendance System offers a practical and efficient solution for attendance management using advanced facial recognition technology. By automating the attendance tracking process, the system reduces manual effort, enhances accuracy, and provides real-time feedback. This makes it an invaluable tool for educational institutions, workplaces, and other environments where attendance tracking is crucial. The system is designed to be scalable and customizable, allowing for easy addition of new images and classes as needed.
