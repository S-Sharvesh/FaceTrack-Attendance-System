# FaceTrack-Attendance-System

Project Description: FaceTrack Attendance System

The FaceTrack Attendance System is an innovative solution designed to streamline attendance tracking using facial recognition technology. This system captures images from a webcam, identifies faces, and marks attendance automatically. Key features of the system include:

Face Encoding and Recognition: The system utilizes face_recognition library to encode faces from a pre-defined set of images and recognize them in real-time through webcam input.
Real-Time Processing: Faces detected in the webcam feed are matched against known encodings, and attendance is marked for recognized individuals.
Attendance Management: Attendance is logged into a CSV file with the name and time of recognition, ensuring that each entry is unique and logged no more than once per hour.
CSV Handling: The system ensures the attendance CSV file is created if it doesn't exist and appends new entries accurately.
User-Friendly Interface: The webcam feed displays bounding boxes and names for recognized faces, providing immediate visual feedback.
Scalability and Customization: The project is designed to be easily scalable, allowing more images and classes to be added as needed.
This project offers a practical and efficient way to monitor attendance, reducing manual effort and enhancing accuracy through advanced facial recognition technology.
