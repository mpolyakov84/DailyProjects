from unittest import TestCase
from unittest import mock
from quotes import write_quote, read_quotes, user_interaction
class TestQuotes(TestCase):

    def test_write_quotes(self):
        actual = 'So many books, so little time.'
        write_quote(actual)
        with open('quotes.txt', 'r') as f:
            quotes = f.readlines()
            expected = quotes[-1]
        self.assertEqual(expected, actual + '\n')

    @mock.patch('quotes.input', return_value='Be yourself; everyone else is already taken.')
    def test_user_interaction(self,mock_input):

        actual = user_interaction()
        with open('quotes.txt', 'r') as file:
            expected = file.read()
        self.assertEqual(expected, actual)