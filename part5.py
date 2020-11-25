import cv2

cv2.namedWindow('window')

def nothing(x):
	pass

cv2.createTrackbar('lower', 'window', 0, 255, nothing)
cv2.createTrackbar('upper', 'window', 0, 255, nothing)

#img = cv2.imread('test.jpg')

cap = cv2.VideoCapture(0)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
	_, img = cap.read()

	img = cv2.blur(img, (3,3))

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	x = cv2.getTrackbarPos('lower', 'window')
	y = cv2.getTrackbarPos('upper', 'window')

	edge = cv2.Canny(gray, x, y)

	cv2.imshow('window', edge)

	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		break
