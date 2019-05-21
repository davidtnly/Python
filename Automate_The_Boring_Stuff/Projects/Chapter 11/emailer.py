#! python3
# emailer.py - Email a string of text

"""
Writer a program that takes an email and string of text on the command line, using selenium, logins your account
and sends an email of the string to the provided address.

Note: Dealing with email can be complicated. Many different users have different settings and use different
types of email accounts. This solution may not work for you. Overall, there are better ways to send emails, which
you will learn later.

Goal: Understand how selenium works
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
User input for credentials
"""
email_user = input('What is your username?\n')
email_pw = input('What is your password?\n')
email_recipient = input('Who would you like to send this email to?\n')
email_subject = input('What is the subject of the email?\n')
email_body = input('What would you like to say?\n')

"""
Use selenium to open up and login to your email
Notes: Adding browser.implicitly_wait(30) to allow browser to load up before keys or clicks
Notes2: You may also want to add time.sleep(5) to give your browser more time to load up
"""
browser = webdriver.Firefox()
browser.implicitly_wait(25)

# Email Address
browser.get('http://mail.google.com')
loginEleme = browser.find_element_by_id('identifierId')
loginEleme.send_keys(email_user)

# Next
nextEleme = browser.find_element_by_id('identifierNext')
nextEleme.click()
time.sleep(3)

# Password
pwEleme = browser.find_element_by_name('password')
pwEleme.send_keys(email_pw)

# Next
pwNextEleme = browser.find_element_by_id('passwordNext')
pwNextEleme.click()
time.sleep(3)

"""
You can select an entire webpage with browser.find_element_by_tag_name('html') and enter your shortcut
keys here. In this example, 'c' will open a new message box then you can send the rest of the keys through TAB & ENTER
"""
htmlEleme = browser.find_element_by_tag_name('html')
htmlEleme.send_keys('c')
htmlEleme.send_keys(Keys.TAB)

htmlEleme.send_keys(email_recipient)
htmlEleme.send_keys(Keys.TAB)

htmlEleme.send_keys(email_subject)
htmlEleme.send_keys(Keys.TAB)

htmlEleme.send_keys(email_body)
htmlEleme.send_keys(Keys.ENTER)

print('Email was sent.')