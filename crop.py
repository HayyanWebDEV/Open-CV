import cv2

image = cv2.imread("strawberryPIC.jpg",-1)
if image is not None:
    print("image loaded")
    crop = image[0:250,0:500]
    cv2.imshow("cropped image",crop)
    cv2.waitKey(0)
else:
    print("image not loaded")