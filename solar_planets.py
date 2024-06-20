import cv2
cv2.imread(“solar-system.jpg”)
cv2.imwrite(“Solar_systemwithname.jpg”,img)

cv2.imshow(“output”,img)
cv2.waitKey(0)

cv2.putText(img,
"Sun",
(20,300),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

 cv2.putText(img,
"Mercury",
(20,350),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

cv2.putText(img,
"Venus",
(20,400),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

cv2.putText(img,
"Earth",
(20,450),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

cv2.putText(img,
"Mars",
(20,500),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

cv2.putText(img,
"Jupiter",
(20,550),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

cv2.putText(img,
"Saturn",
(20,600),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

cv2.putText(img,
"uranus",
(20,650),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

cv2.putText(img,
"naptune",
(20,650),
cv2.FONT_HERSHEY_COMPLEX, 0.5,
(255,255,255)
)

