#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui
import time

print('Press Ctrl-C to quit.')
time_elapsed = 0
start_time = time.time()

try:
    while time_elapsed < 3:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        # Always pass flush=True to print() calls that print \b backspace characters.
        print('\b' * len(positionStr), end=' - ', flush=True)
        time_elapsed = time.time() - start_time
        time.sleep(1)
        print('%s seconds has passed...' % (round(time_elapsed, 0)))

except KeyboardInterrupt:
    print('\nDone.')

print('Finished')
