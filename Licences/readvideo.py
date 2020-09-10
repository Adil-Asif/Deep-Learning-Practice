import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("/home/adilasif/Desktop/Licences/Video.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH,120)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,80)


facecascade = cv2.CascadeClassifier('/home/adilasif/Desktop/Licences/haarcascades/haarcascade_russian_plate_number.xml')




if (cap.isOpened()== False):
    print('Error Reading Video')


while True:
     ret,frame = cap.read()
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     faces = facecascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5, minSize=(25,25))
     kernel= np.ones((5,5),dtype=np.float32)/25
     for (x, y,w, h)in faces:
         abc =cv2.rectangle(frame,(x,y),(x+w, y + h),color=(0,255,0), thickness=2)
         cv2.blur(abc,ksize=(5,5))
        
        
     if ret == True:
          cv2.imshow('Video',frame)
          
          if cv2.waitKey(25) & 0xFF == ord('q'):
            break
     else:
        break


cap.release()
cv2.destroyAllWindows()

