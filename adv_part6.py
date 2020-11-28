import cv2
import numpy as np

hsv = None
lower = []
upper = []

cv2.namedWindow("window2")
def nothing(x):
	pass

def findcolor(event, x, y, flags, param):
	global lower, upper, hsv
	if event == cv2.EVENT_LBUTTONDOWN:
		lower = []
		upper = []
		pixel = hsv[y, x]
		upper.append([(pixel[0]+30)/2, pixel[1]+30, pixel[2]+30])
		lower.append([(pixel[0]-30)/2, pixel[1]-30, pixel[2]-30])
		print(lower, upper)
		cv2.createTrackbar('low h', 'window2', int(lower[0][0]), 179, nothing)
		cv2.createTrackbar('high h', 'window2', int(upper[0][0]), 179, nothing)

		cv2.createTrackbar('low s', 'window2', int(lower[0][1]), 255, nothing)
		cv2.createTrackbar('high s', 'window2', int(upper[0][1]), 255, nothing)

		cv2.createTrackbar('low v', 'window2', int(lower[0][2]), 255, nothing)
		cv2.createTrackbar('high v', 'window2', int(upper[0][2]), 255, nothing)

		


cv2.namedWindow("window")
cv2.setMouseCallback("window", findcolor)


cap = cv2.VideoCapture(0)

track = np.zeros((30,500))

while True:
	#frame = cv2.imread('1.jpg')

	_, frame = cap.read()

	blur = cv2.GaussianBlur(frame, (5,5), 0)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	if len(lower) != 0:

		lh = cv2.getTrackbarPos('low h', 'window2')
		hh = cv2.getTrackbarPos('high h', 'window2')

		ls = cv2.getTrackbarPos('low s', 'window2')
		hs = cv2.getTrackbarPos('high s', 'window2')

		lv = cv2.getTrackbarPos('low v', 'window2')
		hv = cv2.getTrackbarPos('high v', 'window2')

		mask = cv2.inRange(hsv, np.array([lh, ls, lv]), np.array([hh, hs, hv]))
		cv2.imshow("mask", mask)
		contors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

		if contors:
			contors = max(contors, key=cv2.contourArea)

			x,y,w,h = cv2.boundingRect(contors)
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

			cv2.drawContours(frame, contors, -1, (0,255,0), 2)


	cv2.imshow("window", hsv)
	cv2.imshow("window1", frame)
	cv2.imshow("window2", track)

	if cv2.waitKey(1) == 27:
		cap.release()
		cv2.destroyAllWindows()
		break 
