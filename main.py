import cv2
import mediapipe as mp
import time
import HandTrackModule as htm
from pyautogui import *
import pyautogui
import keyboard
import random
import win32api, win32con
import math
import os
import pygame
from pygame.locals import *
import keyboard


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

doigts = [1,1,1,1,1]


mon_dictionnaire = {"Index": "", "Majeur": "", "Annulaire": "", "Auriculaire": "", "Pouce": ""}

def Pause(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(1)

def Avance():
    keyboard.press_and_release('right')
    time.sleep(1)

def Monte():
    keyboard.press_and_release('up')
    time.sleep(1)

def Baisse():
    keyboard.press_and_release('down')
    time.sleep(1)

def Retour():
    keyboard.press_and_release('left')
    time.sleep(1)

def detect_Index():
    if Index > 150: #150
        mon_dictionnaire.update({"Index": "Levé"})
        doigts[0] = 1
    elif Index < 150:
        mon_dictionnaire.update({"Index": "Baissé"})
        doigts[0] = 0

def detect_Majeur():
    if Majeur > 135: #150
        mon_dictionnaire.update({"Majeur": "Levé"})
        doigts[1] = 1
    elif Majeur < 135:
        mon_dictionnaire.update({"Majeur": "Baissé"})
        doigts[1] = 0

def detect_Annulaire():
    if Annulaire > 150: #150
        mon_dictionnaire.update({"Annulaire": "Levé"})
        doigts[2] = 1
    elif Annulaire < 150:
        mon_dictionnaire.update({"Annulaire": "Baissé"})
        doigts[2] = 0

def detect_Auriculaire():
    if Auriculaire > 80: #90
        mon_dictionnaire.update({"Auriculaire": "Levé"})
        doigts[3] = 1
    elif Auriculaire < 80:
        mon_dictionnaire.update({"Auriculaire": "Baissé"})
        doigts[3] = 0

def detect_Pouce():
    if Pouce > 50:
        mon_dictionnaire.update({"Pouce": "Levé"})
        doigts[4] = 1
    elif Pouce < 50:
        mon_dictionnaire.update({"Pouce": "Baissé"})
        doigts[4] = 0

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

        detect_Index()
        detect_Majeur()
        detect_Annulaire()
        detect_Auriculaire()
        detect_Pouce()
        #for i in mon_dictionnaire.items():
            #print(i)
        #os.system("cls")

    if doigts == [1,1,1,1,1]:
        print("ouverte")
    elif doigts == [0,0,0,0,0]:
        print("fermé")
    elif doigts == [1,0,0,0,1]:
        print("Index")
        print("Pause")
        Pause(800, 500)
    elif doigts == [1,1,0,0,1]:
        print("Index, Majeur, Pouce")
        Monte()
    elif doigts == [1,1,1,0,1]:
        print("Index, Majeur, Annulaire, Pouce")
        Baisse()
    elif doigts == [1,1,1,1,0]:
        print("Index, Majeur, Annulaire, Auriculaire")
        Avance()
    elif doigts == [1,0,0,1,1]:
        print("Index,  Auriculaire, Pouce")
        Retour()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
