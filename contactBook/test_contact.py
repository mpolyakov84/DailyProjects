import contact
from contact import user_interaction


def test_user_interaction():
    input_values = ['Max', '12-34', 'test@mail.com', 'y']
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)


    contact.input = mock_input
    contact.print = lambda s: output.append(s)
    user_interaction()

    assert output == ['Welcome to contact book', 'Enter name: ', 'Enter phone number: ', 'Enter email: ',
                      'Contact saved', 'View all contacts? ',
                      'Name: Max \nTelephone: 12-34 \nEmail: test@mail.com']
