import cv2
img = cv2.imread("strawberryPIC.jpg", -1)
if img is not None:
    print("image loaded")
    cv2.imshow("image",img)
    flipped = cv2.flip(img, 1)#0 = top to bottom / 1 = left to right / -1 = both 0&1
    cv2.imshow("flipped image",flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")
