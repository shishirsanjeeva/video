import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)
#read the input image
#img = cv2.imread('36.JPG')
while capture.isOpened():
    _, img = capture.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)

    #display the image
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()



