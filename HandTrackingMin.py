import cv2
import mediapipe as mp
import time

# create our video object
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands() #tulis didalam () sebuah parameter, pencet ctrl dikeyboard dan klik di Hands
# kita gaperlu tulis apa2 didalam () krn didalam Hands sudah ada fungsinya sendiri
mpDraw = mp.solutions.drawing_utils

#ngitung fps
pTime = 0 #previous time
cTime = 0 #current time


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)  #fungsi disamping utk cek apakah sensor tangan bekerja di cam/tidak

    #single hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #get the info of cx and cy information within each of these hands
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                #jika kita ingin mendapat info dri index jari tertentu, bisa coding sperti dibawah
                if id==4:
                    cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time() #akan give us the current time
    fps = 1/(cTime-pTime)
    pTime = cTime

    #display it on the screen jadi kita bisa lihat
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)