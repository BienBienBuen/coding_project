import cv2
import time

vid = cv2.VideoCapture('1.mp4')

pTime = 0
while True:
    success, img = vid.read()
    cv2.imshow("Image", img)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    #在每一帧放字幕
    cv2.putText(img )
    cv2.waitKey(1)