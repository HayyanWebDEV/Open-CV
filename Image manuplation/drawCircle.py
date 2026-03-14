import cv2

img = cv2.imread("strawberryPIC.jpg" , -1)
if img is not None:
    print("image loaded")
    circle = cv2.circle(img,(220,210),135,(200,255,50),3) #-1 for filling entire box
    cv2.imshow("circle on image",circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")