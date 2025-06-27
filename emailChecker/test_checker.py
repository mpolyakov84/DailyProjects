import unittest
from checker import check_email, user_interaction

class TestChecker(unittest.TestCase):

    def test_valid_email1(self):
        result = check_email('case_tes@mail.com')
        self.assertTrue(result)

    def test_invalid_email1(self):
        result = check_email('test.mai.org')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
