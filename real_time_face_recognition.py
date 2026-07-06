# ==========================================
# Real-Time Face Recognition
# Version 1.0
# Author: Danial Barjasteh
# ==========================================
"""
Real-Time Face Recognition

Author: Danial Barjasteh
Version: 1.0
Language: Python

Libraries:
    - OpenCV
    - face_recognition

Description:
This project performs real-time face recognition using a webcam.
It detects a face, generates its face encoding, compares it with a
pre-encoded known face, and displays the person's name above the
detected face if a match is found.

Current Features:
    - Real-time webcam capture
    - Face detection
    - Face encoding
    - Face comparison
    - Bounding box around detected face
    - Name labeling for recognized faces

Future Improvements:
    - Multiple face recognition
    - Face distance for more accurate matching
    - FPS optimization
    - Confidence score display
    - Cleaner project structure
"""

#----------------------------------------------------------------------
#                          IMPORTS LIBRARIES
#----------------------------------------------------------------------
import face_recognition as fr
import cv2

#----------------------------------------------------------------------
#                    LOAD AND ENCODE MY PICTURE
#----------------------------------------------------------------------
person = fr.load_image_file("images/test_image.jpg")
known_face_name  = "Danial"
known_face_encoding  = fr.face_encodings(person)[0]


#----------------------------------------------------------------------
#                START PROGRAM WITH OPEN THE CAMERA
#----------------------------------------------------------------------
video = cv2.VideoCapture(0)

while True:
    
    # Read image
    ret,img = video.read()
    if not ret:
        break
    img = cv2.flip(img,1)
    small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    # Finding the coordinates of the face
    locate = fr.face_locations(small_img)
    
    if locate:

        # Encoding the image
        encoding = fr.face_encodings(small_img,locate)
        
        # Extract face coordinates
        top, right, bottom, left = locate[0]

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        # Draw bounding box around the detected face
        cv2.rectangle(img,(left,top),(right,bottom),(0,123,0),3)
        
        # Compare detected face with known face
        if encoding:
            img_encode = encoding[0]
            compare_result = fr.compare_faces([known_face_encoding],img_encode)
            
            # Display recognition result on the frame
            print(compare_result,": ",end=" ")
            
            if compare_result[0]:
                cv2.putText(img,known_face_name,(left,top-20),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,123,0),4)
                print(known_face_name)
            else:
                cv2.putText(img,"####",(left,top-20),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,123),4)
                print("unknown")
    
    # Show image
    cv2.imshow("Face Recognition",img)
    
    # for exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
