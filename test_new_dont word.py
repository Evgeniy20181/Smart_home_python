import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
sgodztvo = 0
etalon = cv2.imread('./Evgeniy/etalon.png')
etalon = cv2.resize(etalon,(128,128))
faceCascade = cv2.CascadeClassifier('lico.xml')
f = open('text.txt', 'w')
f.write("flag_null")
f.close()
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(30, 30)
    )

    for (x,y,w,h) in faces:
        sgodztvo = 0
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray,(128,128))
        f = open('text.txt', 'r')
        content = str(f.read())
        f.close()
        if content == "flag_null":
            f = open('text.txt', 'w')
            etalon_two_two = roi_gray
            f.write("flag_up")
            f.close()
            
       # roi_color = img[y:y+h, x:x+w]

        cv2.imshow("cut",roi_gray)
        cv2.imwrite("foto_face.png",roi_gray)
        time.sleep(0.1)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        print("Img from cam")
        print(roi_gray)
        print("Etalon")
        print(etalon_two_two)
        #face_gray_foto = cv2.imread('./foto_face.png')
        for x in range(128):
            for y in range(128):
                if etalon_two_two[x][y] == etalon[x][y]:
                    print("ok")
                    

    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
