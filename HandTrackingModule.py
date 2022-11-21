# mencoba menentukan value dari thumb
import cv2
import mediapipe as mp
import time
#main reason dri make module ini adalah utk get those position values of the landmarks dgn gampang
#dan kita bisa pake module ini di different project
class handDetector():
    def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon,
                                        self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)  #fungsi disamping utk cek apakah sensor tangan bekerja di cam/tidak

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw= True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img,(cx, cy), 10, (255, 0, 255), cv2.FILLED)

        return lmlist

#dibawah ini adalah dummy code, dummy code ini bisa kita pake utk run di different project
def main():
    # ngitung fps
    pTime = 0  # previous time
    cTime = 0  # current time
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            print(lmlist[4]) # print value dari mylist di any index, jika kita mau index 0, ya tulis 0
        #if len(lmlist) != 0:
            #print(lmlist[4])
        #nanti akan work seperti x_position(mendatar) akan berubah seiring bergerak, dan y_position(tegak) juga akan berubah jika bergerak keatas

        cTime = time.time()  # akan give us the current time
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # display it on the screen jadi kita bisa lihat
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()