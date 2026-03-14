import cv2
img = cv2.imread('strawberryPIC.jpg' , -1)
if img is not None:
    print("image loaded")
    imgWithText = cv2.putText(img,'halo this is a strawberry',(50,50),cv2.FONT_ITALIC,1.0,(255,0,255), 3)
    cv2.imshow("imgWithText",imgWithText)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")