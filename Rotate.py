import cv2
img = cv2.imread("strawberryPIC.jpg",-1)
if img is not None:
    print("image loaded")
    cv2.imshow("image",img)
    imShape = img.shape
    w,h = imShape[0],imShape[1]
    centerpoint = (w // 2 , h // 2)
    M = cv2.getRotationMatrix2D(centerpoint,45,0.5)
    rotated = cv2.warpAffine(img,M,(w,h))
    cv2.imshow("rotated",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image not loaded")