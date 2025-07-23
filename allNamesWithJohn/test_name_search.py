import unittest
from name_search import search_names, user_interaction
from unittest import mock


class TestNameSearch(unittest.TestCase):

    def test_search_names_positive(self):
        test_result = search_names('John')
        expected_result = ['John Smith', 'John Doe', 'John Williams']
        self.assertEqual(expected_result, test_result)

    def test_search_names_negative(self):
        test_result = search_names('Max')
        expected_result = []
        self.assertEqual(expected_result, test_result)

    @mock.patch('name_search.input')
    def test_user_interaction(self, mock_input):

        mock_input.side_effect = ['John']
        actual_result = user_interaction()
        expected_result = ['John Smith', 'John Doe', 'John Williams']
        self.assertEqual(expected_result, actual_result)
