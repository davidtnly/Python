#! python3
# strong_password_detection.py
"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that
is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string
against multiple regex patterns to validate its strength.
"""

import re

# First, create regex's that meet all expectations given by the problem. There should be
# 1) at least 8 characters
# 2) at least one upper case
# 3) at least one lower case
# 4) at least one number
# Regex can be tricky! Make sure you have all symbols, parentheses, and escape characters
# placed in the correct spot. This may take some practice! It may help to test each regex
# one at a time until you get used to it.
length_regex = re.compile('.{8,}')  # 8 characters long
lower_case_regex = re.compile('[a-z]+')  # contains lowercase characters
upper_case_regex = re.compile('[A-Z]+')  # contains uppercase characters
digit_regex = re.compile('[\d]+')  # contains at least 1 digit

# Create a regex list of of the ones created above.
regex_list = [length_regex,
              lower_case_regex,
              upper_case_regex,
              digit_regex]

# For this, I initiated a regex_count and set it to 0 right when the function starts. This will
# be used later if the password meets expectations. The for loops will loop over each regex and
# break out of the loop if it doesn't meet one of the criteria. If it makes it through each one
# successfully, regex_count adds a 1 to its value. Once the loop is finished and has 4 successful
# regex searches then it will print a message saying your password is strong enough.
def strong_password(password):
    regex_count = 0
    count = 0
    # loop through each re.compile()
    for regex in regex_list:
        print(count)
        if regex.search(password) is None:
            print('Sorry, your password is not strong enough')
            print('on count: ' + str(count))
            if count == 0:
                print('Failed password length')
            elif count == 1:
                print('Failed lowercase requirement')
            elif count == 2:
                print('Failed uppercase requirement')
            else:
                print('Failed digit requirement')
            print('Failed Regex: ' + str(regex))
            print(regex.search(password))
            break
        else:
            regex_count += 1
            count += 1
            continue
    if regex_count is 4:
        print('Congrats. Your password is strong enough!')


pw = input('Please type in a password:\n')
strong_password(pw)


# Below is a list of passwords you can test. Copy it into your code and remove the comments
# pw_test1 = 'testpw'
# pw_test2 = 'Testpw'
# pw_test3 = 'TESTPW'
# pw_test4 = 'TESTPW123'
# pw_test5 = 'Testpw123'
# pw_test6 = 'TESTPW123!@#'
# pw_test7 = 'Tb1@Tb1@'
# pw_test8 = 'TestPW123'
# pw_test9 = '!@345ssfe@#23T4'
#
# strong_password(pw_test1)
# strong_password(pw_test2)
# strong_password(pw_test3)
# strong_password(pw_test4)
# strong_password(pw_test5)
# strong_password(pw_test6)
# strong_password(pw_test7)
# strong_password(pw_test8)
# strong_password(pw_test9)

"""
This is an alternate way you can write this function. If you don't want to iterate through a loop
and add a count iterator, then you can create an if loop with each regex separately. The first time
it fails it will return a statement saying your password isn't strong enough. If it makes it through
the end then the password is strong enough
def is_strong_pw(password):
    if pw_reg_1.search(password) is None:
        return 'Your password is not strong enough'
    if pw_reg_2.search(password) is None:
        return 'Your password is not strong enough'
    if pw_reg_3.search(password) is None:
        return 'Your password is not strong enough'
    if pw_reg_4.search(password) is None:
        return 'Your password is not strong enough'
    if pw_reg_5.search(password) is None:
        return 'Your password is not strong enough'
    else:
        return 'Congrats! Your password will suffice!'
pw_reg_1 = re.compile(r'[a-z]+')
pw_reg_2 = re.compile(r'[A-Z]+')
pw_reg_3 = re.compile(r'[0-9]+')
pw_reg_4 = re.compile(r'[!@#$^&*()]+')
pw_reg_5 = re.compile(r'.{8,}')
"""