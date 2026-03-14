import cv2

image = cv2.imread('strawberryPIC.jpg' , -1)
if image is not None:
    print("image loaded")
    resized = cv2.resize(image,(1920 ,1080))
    cv2.imshow("image",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")