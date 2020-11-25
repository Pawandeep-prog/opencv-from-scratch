import cv2
import numpy as np

run = False

def draw(event, x, y, flag, param):
	global run

	if event == cv2.EVENT_LBUTTONDOWN:
		run = True
		cv2.circle(win, (x,y), 5 , (0,255,0), 2)

	if event == cv2.EVENT_LBUTTONUP:
		run = False

	if event == cv2.EVENT_MOUSEMOVE:
		if run == True:
			cv2.circle(win, (x,y), 5 , (0,0,255), 2)

	if event == cv2.EVENT_RBUTTONDOWN:
		cv2.rectangle(win, (x,y), (x+30, y+30), (255,0,0), 3)

cv2.namedWindow('window')
cv2.setMouseCallback('window', draw)

win = np.zeros((500,500,3), dtype='float64')

while True:

	cv2.imshow('window', win)

	k = cv2.waitKey(1)

	if k == ord('c'):
		win = np.zeros((500,500,3), dtype='float64')

	if k == 27:
		cv2.destroyAllWindows()
		break










