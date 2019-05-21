#! python3
# game_2048.py - Launch a game of 2048 and play automatically

"""
2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys.
You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and over
again.

Write a program that will open the game at: https://gabrielecirulli.github.io/2048/ and keep sending up, right,
down, and left keystrokes to automatically play the game.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

"""
Using selenium and your appropriate webdriver, open the game and maximize your window
"""

"""
Step one: open up browser of your choice and get to the url
"""
browser = webdriver.Firefox()
url = 'https://gabrielecirulli.github.io/2048/'
browser.get(url)
# browser.maximize_window()

"""
Step two: obtain the HTML element that will allow you to utilize your Keys on the webpage
"""
htmlElem = browser.find_element_by_tag_name('html')

"""
Step three: While True will run this continuously. Use the random module to allow a random key to be pressed
so it's not the same pattern over and over. If you use Try/Except statement at the end of your keypress to try
and click the retry-button after a game complets, you can have the program automatically start a game.

Limit your turns so the program does not run infinitely so instead of while True use while turn < #
"""
turns = 0
while turns < 10000:
    key = random.randint(1, 4)
    turns += 1
    if key is 1:
        htmlElem.send_keys(Keys.UP)
    elif key is 2:
        htmlElem.send_keys(Keys.DOWN)
    elif key is 3:
        htmlElem.send_keys(Keys.RIGHT)
    elif key is 4:
        htmlElem.send_keys(Keys.LEFT)
    try:
        retryElem = browser.find_element_by_class_name('retry-button')
        retryElem.click()
        continue
    except:
        continue