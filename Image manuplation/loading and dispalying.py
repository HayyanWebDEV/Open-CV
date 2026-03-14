import cv2

image = cv2.imread('strawberryPIC.jpg' , 0)

if image is not None:
    cv2.imshow('Strawberry',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not image can't be loaded")
