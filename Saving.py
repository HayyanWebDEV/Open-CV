import cv2

image = cv2.imread('strawberryPIC.jpg' , 1)

if image is not None:
    print("image loaded successfully")
    save = cv2.imwrite('NewstrawberryPIC.jpg', image)
    if save:
        print("image saved successfully")
    else:
        print("image not saved")
else:
    print("image can't be loaded")
