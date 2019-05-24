#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui
import time

time_elapsed = 0
start_time = time.time()
print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        # Always pass flush=True to print() calls that print \b backspace characters.
        print('\b' * len(positionStr), end='', flush=True)
        time_elapsed = time.time() - start_time
        time.sleep(1)
        print('%s seconds has passed...' % (round(time_elapsed, 0)))

except KeyboardInterrupt:
    print('\nDone.')
