import cv2
image = cv2.imread('NewstrawberryPIC.jpg', 1)
if image is not None:
    print("image loaded")
    height, width , colorChannels = image.shape
    print(f"image is loaded\n height : {height}\n width : {width}\n color channels : {colorChannels}")
