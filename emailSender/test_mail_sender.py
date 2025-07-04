import mail_sender
import unittest
import re


# NOT ACTUAL: check send_email - negative/positive


def check_email(email):
    pattern = r"^[\w._+-]+@[\w_+-]+\.[\w_+-]+$"
    if re.match(pattern, email):
        return True
    else:
        return False


class TestMailSender(unittest.TestCase):

    def test_password_exists(self):
        result = mail_sender.get_pass()
        self.assertIsNotNone(result)

    def test_recipients_list(self):
        result = mail_sender.get_recipient_list()
        self.assertIsNotNone(result)

    def test_check_emails(self):
        recipients = mail_sender.get_recipient_list()
        for recipient, name in recipients:
            result = check_email(recipient)
            self.assertTrue(result)
