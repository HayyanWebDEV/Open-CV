import cv2

img = cv2.imread("strawberryPIC.jpg" , -1)
if img is not None:
    print("image loaded")
    rectangle = cv2.rectangle(img,(50,90),(330,330),(0,100,255),3) #-1 for filling entire box
    cv2.imshow("rectangle on image",rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")