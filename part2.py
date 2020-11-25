import cv2

img = cv2.imread('image.jpg')

while True:

	cv2.line(img, (265,40), (128,230), (0,0,255), 2)

	cv2.rectangle(img, (256,87), (380,150), (0,255,0), 2)

	cv2.circle(img, (160,60), 40, (255,0,0), 2)

	cv2.putText(img, "subscribe", (40,330), cv2.FONT_HERSHEY_SIMPLEX,2,
	(0,0,255), 2)

	cv2.imshow("window", img)

	if cv2.waitKey(0) == 27:
		break

cv2.destroyAllWindows()

