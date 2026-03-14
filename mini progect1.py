import cv2

address = input("enter file address: ")
if address is not None:
    image = cv2.imread(address,-1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show = input("Show image or not (y/n): ").lower()
    if show == "y":
        imageName = input("enter name you want to show: ")
        cv2.imshow(imageName,gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("Newimage.jpg",gray)
        print("image saved")
    else:
        print("image not saved and showed")
else:
    print("image not loaded")


