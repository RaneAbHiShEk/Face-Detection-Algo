import cv2
#imagepath="C:\\Users\\Abhishek Rane\\Desktop\\people.jpg"
cascpath="C:\\Users\\Abhishek Rane\\Desktop\\classifier1.xml"
facecascade=cv2.CascadeClassifier(cascpath)
image=cv2.imread('C:\\Users\\Abhishek Rane\\Desktop\\people.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
#print("found {0} faces in image").format(len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("facesfound",image)
cv2.waitKey(0)
