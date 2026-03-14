import cv2


def save_image(img):
    save_choice = input("you want to save the image? (y/n): ").lower()
    if save_choice == 'y':
        save_name = input("enter your file name for saving new image: ")
        success = cv2.imwrite(save_name,img)
        if success:
            print("image saved")
        else:
            print("image can not be saved")
    else:
        print("image not saved")


def get_color():
    b , g , r = input("enter your color in bgr format: ").strip().split(" ")
    color = (int(b) , int(g) , int(r))
    return color


def draw_line(image):
    x1 = int(input("enter x1 for point1: "))
    y1 = int(input("enter y1 for point1: "))
    x2 = int(input("enter x2 for point2: "))
    y2 = int(input("enter y2 for point2: "))
    pt1 = (x1, y1)
    pt2 = (x2, y2)
    color = get_color()
    thickness = int(input("enter your thickness for line: "))
    lined_image = cv2.line(image,pt1,pt2,color,thickness)
    save_image(lined_image)
    cv2.imshow("lined_image",lined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_rectangle(image):
    x1 = int(input("enter x1 for point1: "))
    y1 = int(input("enter y1 for point1: "))
    x2 = int(input("enter x2 for point2: "))
    y2 = int(input("enter y2 for point2: "))
    pt1 = (x1, y1)
    pt2 = (x2, y2)
    color = get_color()
    thickness = int(input("enter your thickness for rectangle (-1 if you want to fill the rectangle): "))
    rectangle_image = cv2.rectangle(image,pt1,pt2,color,thickness)
    save_image(rectangle_image)
    cv2.imshow("rectangle on image",rectangle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_circle(image):
    x = int(input("enter x for center point: "))
    y = int(input("enter y for center point: "))
    radius = int(input("enter radius for the circle: "))
    center = (x, y)
    color = get_color()
    thickness = int(input("enter your thickness for circle (-1 if you want to fill the circle): "))
    circle_image = cv2.circle(image,center,radius,color,thickness)
    cv2.imshow("circle on image",circle_image)
    save_image(circle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def put_text(image):
    x = int(input("enter x for origin point: "))
    y = int(input("enter y for origin point: "))
    origin = (x, y)
    text = input("enter your text: ")
    color = get_color()
    thickness = int(input("enter your thickness for text: "))
    font_scale = int(input("enter your font scale (1 = normal, 2 = big): "))
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_image = cv2.putText(image,text,origin,font,font_scale,color,thickness)
    cv2.imshow("text on image",text_image)
    save_image(text_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image_drawing(file_location):
    img = cv2.imread(file_location,-1)
    if img is not None:
        print('image loaded')
        drawing_choice = int(input("enter your choice: \n1.draw a line \n2.draw a rectangle \n3.draw a circle\n4.put a text (1/2/3/4):"))
        if drawing_choice == 1:
            draw_line(img)
        elif drawing_choice == 2:
            draw_rectangle(img)
        elif drawing_choice == 3:
            draw_circle(img)
        elif drawing_choice == 4:
            put_text(img)
        else:
            print("invalid choice")
    else:
        print("image not loadedWrong file location")

file_location1 = input("enter your file location: ")
image_drawing(file_location1)