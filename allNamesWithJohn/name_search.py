def search_names(name='John'):
    """
    Search for all names with the given name.
    :param name:
    :return: list of full names
    """
    result = list()
    with open('names.txt','r') as f:
        names = f.read().splitlines()
    for itm in names:
        if name.lower() == itm.strip('\n').split()[0].lower():
            result.append(itm)
    return result

def user_interaction():
    """
    Func to interact with user to search for names.
    :return: list of names
    """
    input_name = input('Enter the name to look for: ')
    result = search_names(input_name)

    if len(result) == 0:
        print(f'None name found starting with \n \'{input_name}\'')
    else:
        print(f'There are all the names starting with: \'{input_name}\'')
        for name in result:
            print(name)
