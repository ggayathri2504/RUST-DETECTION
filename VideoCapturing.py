import cv2
import numpy as np

#capturing video
cap = cv2.VideoCapture(0)

#trackerbar for accurate point
"""cv2.namedWindow("Tracker")

cv2.createTrackbar("l_r", "Tracker", 0, 180, none)
cv2.createTrackbar("l_g", "Tracker", 0, 255, none)
cv2.createTrackbar("l_b", "Tracker", 0, 255, none)
cv2.createTrackbar("u_r", "Tracker", 180, 180, none)
cv2.createTrackbar("u_g", "Tracker", 255, 255, none)
cv2.createTrackbar("u_b", "Tracker", 255, 255, none)"""


#extracting image from video       
while True:
    _, frame = cap.read()
    cv2.imwrite('normal_image.jpeg', frame)
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2RGB)  
    
    #setting points
    """l_r = cv2.getTrackbarPos("l_r", "Tracker")
    l_g = cv2.getTrackbarPos("l_g", "Tracker")
    l_b = cv2.getTrackbarPos("l_b", "Tracker")
    u_r = cv2.getTrackbarPos("u_r", "Tracker")
    u_g = cv2.getTrackbarPos("u_g", "Tracker")
    u_b = cv2.getTrackbarPos("u_b", "Tracker")"""
   
    """lower_blue = np.array([52,54,59])
    upper_blue = np.array([185,200,205])"""
    
    lower_blue = np.array([55,58,59])
    upper_blue = np.array([180,187,184])
    
    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    
    lower_red = np.array([30,150,50]) 
    upper_red = np.array([255,255,180])
    
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    
    res = cv2.bitwise_and(frame,frame, mask=mask_red)
    
    edges = cv2.Canny(frame,100,200)
    
    cv2.imshow('Edges',edges) 
    #_, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
     
    #for contour in contours:
     #   area = cv2.contourArea(contour)
      #  if area > 1000:
       #     cv2.drawContours(frame, contour,-1, (0,255,0), 3)
   
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imwrite('contours_image.jpeg', frame)
    cv2.imwrite('hsv_image.jpeg', mask)
    cv2.imwrite('edges_image.jpeg',edges)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
       

cap.release()
cv2.destroyAllWindows()
