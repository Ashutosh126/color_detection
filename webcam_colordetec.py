import cv2
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    _, frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height,width, _=frame.shape
    
    cx=int(width/2)
    cy=int(height/2)
    
    pixel_center= hsv_frame[cy,cx]
    hue=pixel_center[0]
    
    color="Undefined"
    if (0 <= hue < 15 or 165 <= hue <= 180):
        color="RED"
    elif 15 <= hue < 30:
        color="Orange"
        
    elif 30 <= hue < 60:
        color="Yellow"
    elif 60 <= hue < 90:
    
        color="Green"
    elif 90 <= hue < 120:
        color="Blue"
    elif 120 <= hue < 150:
        color="Blue"
    elif 150 <= hue < 165:    
         color="Voilet"
    else:
        color="Red"
    pixel_center_bgr=frame[cy,cx]
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    
    cv2.putText(frame,color,(10,70),0,1.5,(b,g,r),2)
    
    
    cv2.circle(frame,(cx,cy),5,(25,25,25),3)
    
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()

# img=cv2.imread("pexels-magda-ehlers-636353.jpg")


# # print(img)

# cv2.imshow("Img",img)

# cv2.waitKey(0)