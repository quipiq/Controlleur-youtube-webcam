import cv2
import mediapipe as mp
import time
import HandTrackModule as htm
import math


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x1, y1 = lmList[0][1], lmList[0][2] #Centre poignet
        x2, y2 = lmList[8][1], lmList[8][2] #Haut Index
        x3, y3 = lmList[12][1], lmList[12][2] #haut Majeur
        x4, y4 = lmList[16][1], lmList[16][2] #haut Annulaire
        x5, y5 = lmList[20][1], lmList[20][2] #haut Auriculaire
        x6, y6 = lmList[4][1], lmList[4][2] #haut pouce
        #print(lmList)
        Index = math.hypot(x2 - x1, y2 - y1)
        Majeur = math.hypot(x3 - x1, y3 - y1)
        Annulaire = math.hypot(x4 - x1, y4 - y1)
        Auriculaire = math.hypot(x5 - x1, y5 - y1)
        Pouce = math.hypot(x6 - x1)
        if Pouce > 50: #150
            print("Levée")
        elif Pouce < 50:
            print("Baissée")

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
