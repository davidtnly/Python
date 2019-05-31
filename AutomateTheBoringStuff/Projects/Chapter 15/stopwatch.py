#! python3
# stopwatch.py - Stopwatch function with 'pretty' output as well as copying to clipboard

import time
import pyperclip


# Set variables
start_time = time.time()
last_time = start_time
lap_num = 1
lines = []  # empty list to store values

# while Loop through time and laps
try:
    while lap_num < 10:
        input()
        line = ''
        lap_time = format(round(time.time() - last_time, 2), '.2f')
        total_time = format(round(time.time() - start_time, 2), '.2f')
        lapNum = 'Lap #%s: ' % str(lap_num)
        totalTime = str(total_time).rjust(5)
        lapTime = ' (%s)' % str(lap_time).rjust(5)
        totalPrint = (lapNum + totalTime + lapTime)
        print(totalPrint, end='')
        lines.append(totalPrint)
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its erro message frm displaying
    print('\nDone')

# The join() method takes an iterable - objects capable of returning its members one at a time
text = '\n'.join(lines)
pyperclip.copy(text)
