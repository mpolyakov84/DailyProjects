import unittest
from unittest import mock
from sum_numbers import usr_interaction


class SumAllNumbersTest(unittest.TestCase):

    @mock.patch('sum_numbers.input', create=True)
    def test_user_interaction(self,mock_input):
        mock_input.side_effect = [3,5]
        result = usr_interaction()
        self.assertEqual((3,5), result)