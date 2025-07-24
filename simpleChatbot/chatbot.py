# App is a Simple Python Chatbot That Talks BackBuild a Simple Python Chatbot That Talks Back

def input_analyzer(mes='d'):
    """
    Func analyse str and return required answer
    :param mes: str - input from user
    :return: Answer from chatbot
    """
    input_list = mes.lower().split()

    greeting_list = ['hi', 'hello']
    farewell_list = ['exit', 'quit', 'q', 'bye']

    if any(x in input_list for x in greeting_list):
        return 'Chatbot: Hi there! How can I help you today?'

    elif any(x in input_list for x in farewell_list):
        print('Chatbot: Goodbye! Have a nice day!')
        return None

    else:
        return "Chatbot: I’m not sure how to respond to that."


def chatbot():
    """
    Interaction with user
    :return:
    """
    print('Chatbot: Hello! I am a simple chatbot. Type something to start talking '
          '(or type \'exit\' to quit).\' )')
    while True:
        user_input = input('You: ')
        bot_answer = input_analyzer(user_input)

        if bot_answer is None:
            break
        else:
            print(bot_answer)

