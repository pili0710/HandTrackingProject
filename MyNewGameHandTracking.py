# mencoba module di project baru, jadi gaperlu nulis semua code nya :D
import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0  # previous time
cTime = 0  # current time
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
                print(lmlist[4])  # print value dari mylist di any index, jika kita mau index 0, ya tulis 0
        # if len(lmlist) != 0:
        # print(lmlist[4])
        # nanti akan work seperti x_position(mendatar) akan berubah seiring bergerak, dan y_position(tegak) juga akan berubah jika bergerak keatas

        cTime = time.time()  # akan give us the current time
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # display it on the screen jadi kita bisa lihat
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)