import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

	_, frame  = cap.read()

	hsv = cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)

	lower = np.array([45,200,20])
	upper = np.array([65,250,250])

	mask = cv2.inRange(hsv, lower, upper)

	contors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	if contors:
		contors = max(contors, key=cv2.contourArea)

		x,y,w,h = cv2.boundingRect(contors)

		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

		cv2.drawContours(frame, contors, -1, (0,225,0), 2)

	cv2.imshow("window", frame)
	cv2.imshow("window1", hsv)
	cv2.imshow("window2", mask)

	if cv2.waitKey(1) == 27:
		cap.release()
		cv2.destroyAllWindows()
		break