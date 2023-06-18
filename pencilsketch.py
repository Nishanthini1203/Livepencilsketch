import cv2
def image_to_sketch(img, k_size=45):
    #Read Image
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    sketch_img=cv2.divide(grey_img,invblur_img, scale=250.0)
    cv2.imwrite("sketch_img.jpg",sketch_img)
    return sketch_img
    
    
#Function call
cap=cv2.VideoCapture(0)
while 1:
    ret,frame=cap.read();
    cv2.imshow('sketch image',image_to_sketch(frame))
    if cv2.waitKey(1)=='q':
        break
cap.release()
cv2.destroyAllWindows()
