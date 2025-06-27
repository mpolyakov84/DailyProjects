#app checks if an email address is valid using regex in Python
import re
# TODO: unittest

def check_email(email):
    pattern = r"^[\w._+-]+@[\w_+-]+\.[\w_+-]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

def user_interaction():

    while True:
        email = input('Enter an email to check if it\'s valid : ')
        if check_email(email):
            print('That\'s a valid email address!')
            break
        else:
            print('That\'s not a valid email address!')

user_interaction()