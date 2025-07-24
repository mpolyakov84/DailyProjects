import unittest
from unittest import mock
from chatbot import input_analyzer,chatbot

class TestChatbot(unittest.TestCase):

    def test_input_analyzer(self):
        actual_result = input_analyzer('Hello')
        expected_result = 'Chatbot: Hi there! How can I help you today?'
        self.assertEqual(expected_result, actual_result)

    @mock.patch('chatbot.input')
    def test_chatbot(self, mock_input):
        mock_input.side_effect = ['bye']
        actual_result = chatbot()
        expected_result = 'Test'
        self.assertEqual(expected_result, actual_result)
