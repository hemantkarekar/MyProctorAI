import cv2
import os
from flask import flash

camera = cv2.VideoCapture(0)
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''
def generate_frames():  
    while True:
        # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            img_counter = 0
            k = cv2.waitKey(1)
            if k%256 == 32:
                path = "E:/MSc IT/Project/MyProctorAI"
                cv2.imwrite(os.path.join(path,"opencv_frame_%d.png" %img_counter), frame)
                # cv2.imwrite("opencv_frame_%d.png" %img_counter, frame)
                print("Image Captured:", success)
            img_counter+=1 
            # capture_demo(frame)
            detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
            eyes_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
            faces = detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0,), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0),2)
            ret, buffer = cv2.imencode('.jpg', frame) 
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result