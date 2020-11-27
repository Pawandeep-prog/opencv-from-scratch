import cv2
import numpy as np

cv2.namedWindow('window')

def nothing(x):
	pass

cv2.createTrackbar('low h', 'window', 0, 179, nothing)
cv2.createTrackbar('high h', 'window', 0, 179, nothing)

cv2.createTrackbar('low s', 'window', 0, 255, nothing)
cv2.createTrackbar('high s', 'window', 0, 255, nothing)

cv2.createTrackbar('low v', 'window', 0, 255, nothing)
cv2.createTrackbar('high v', 'window', 0, 255, nothing)

cap = cv2.VideoCapture(0)

tracks = np.zeros((10,500))



while True:
	_, frame = cap.read()
	frame = cv2.GaussianBlur(frame, (3,3), 5)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lh = cv2.getTrackbarPos('low h', 'window')
	hh = cv2.getTrackbarPos('high h', 'window')

	ls = cv2.getTrackbarPos('low s', 'window')
	hs = cv2.getTrackbarPos('high s', 'window')

	lv = cv2.getTrackbarPos('low v', 'window')
	hv = cv2.getTrackbarPos('high v', 'window')

	lower = np.array([lh,ls,lv])
	upper = np.array([hh,hs,hv])

	mask = cv2.inRange(hsv, lower, upper)

	contors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	if contors:
		contors = max(contors, key=cv2.contourArea)

		x,y,w,h = cv2.boundingRect(contors)
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

		cv2.drawContours(frame, contors, -1, (0,255,0), 2)

	cv2.imshow("mask", mask)
	cv2.imshow("window2", frame)
	cv2.imshow('window', tracks)



	if cv2.waitKey(1) == 27:
		cap.release()
		cv2.destroyAllWindows()
		break

