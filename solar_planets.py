import cv2

img = cv2.imread("poster.jpg")

cv2.putText(img,  
           "sun",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Jupiter",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Saturn",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Uranus",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Neptune",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.imshow("output",img)

cv2.waitKey(0)