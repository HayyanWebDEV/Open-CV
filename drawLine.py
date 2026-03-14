import cv2

img = cv2.imread("strawberryPIC.jpg",-1)
if img is not None:
    print("image loaded")
    lined = cv2.line(img,(100,50),(500,50),(0,255,255),3)
    cv2.imshow("lined image",lined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")