#! python 3
# spiralDraw.py

import pyautogui as pag
import time

pag.click()
distance =
startTime = time.time()

while distance > 0:
    pag.dragRel(distance, 0, duration = 0.2) # move right
    distance = distance - 5
    pag.dragRel(-distance, 0, duration = 0.2) # move left
    distance = distance - 5
    pag.dragRel(0, -distance, duration = 0.2) # move up