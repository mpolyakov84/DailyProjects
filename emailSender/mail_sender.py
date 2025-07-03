# Bulk email sender from CSV with PythonBulk email sender from CSV with Python

import yagmail
import os
import pandas as pd
from dotenv import load_dotenv,find_dotenv

def get_pass():
    '''
    Function to get a  password.
    :return: 
    '''''
    load_dotenv(find_dotenv(), override=True)
    password = os.getenv('PASSWORD')
    return password

def send_email(recipient, subject, body, sender = 'mpolyakov7@gmail.com'):
    '''
    Function to send an email.
    :param recipient:
    :param subject:
    :param body:
    :param sender:
    :return: True if the email was sent, False otherwise.
    '''
    try:
        password = get_pass()
        yag = yagmail.SMTP(sender,password)
        yag.send(recipient, subject, body)
        print(f'Email has been sent to {recipient}!')
        return True
    except:
        return False


def get_recipient_list():
    '''
    Function to get a list of recipients from csv file.
    :return: list of recipients lists
    '''
    df = pd.read_csv('emails_accounts.csv')
    recipients = df.values.tolist()
    return recipients

def main():
    recipients = get_recipient_list()
    for recipient, name in recipients:
        subject = f'Personal notification for {name}!'
        body = f'''
        Hello {name}!
        This email has been created automatically.
        This is just for test app
        Best Regards!
        '''
        send_email(recipient, subject, body)


# TODO: authentication and func for password - DONE
# TODO: Read emails from csv - DONE
# TODO: Send emails to recipients - DONE
# TODO: Write unit tests
