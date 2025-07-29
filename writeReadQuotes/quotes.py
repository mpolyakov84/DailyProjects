# App Write and Read a Quote Using Python


def write_quote(quote):
    """
    Writes quote to file.
    :param quote:
    :return:
    """
    with open('quotes.txt', 'a') as f:
        f.write(quote+'\n')
        f.close()


def read_quotes():
    """
    Reads quotes from file.
    :return: all quotes
    """
    with open('quotes.txt', 'r') as f:
        lines = f.read()
    return lines


def user_interaction():
    """
    Function interacts with user to enter quotes.
    :return:
    """
    user_input = input("What is your favorite quote? \n")
    write_quote(user_input)
    quotes = read_quotes()
    print('Saved and loaded quote: \n', quotes)
