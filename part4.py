import cv2
import numpy as np

img = cv2.imread('image.jpg')

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.blur(img, (2,2))
#img = cv2.GaussianBlur(img, (5,5), 10)
#_, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
#img2 = cv2.erode(img, np.ones((5,5)), iterations=3)

img = img[80:220, 210:410]

while True:
	cv2.imshow('original', img)

	if cv2.waitKey(0) == 27:
		cv2.destroyAllWindows()
		break