#! python3
# countdown.py - simple countdown script

import time
import subprocess

timeleft = 60

while timeleft > 0:
    print(timeleft, end='')
    time.sleep(1)
    timeleft = timeleft-1

# Play sound file when 0
subprocess.Popen(['start', 'alarm.wav'], shell=True)