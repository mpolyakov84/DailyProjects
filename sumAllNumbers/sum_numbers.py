# App Sum All Numbers in a User-Defined Range with Python


def sum_numbers(num_range):
    """
    Returns the sum of all numbers between start_range and end_range.
    :param num_range: tuple[int] range of numbers:
    :return: sum(int)
    """
    num_sum = 0
    for i in range(num_range[0], num_range[1]+1):
        num_sum += i
    return num_sum


def usr_interaction():
    """
    Asks the user to enter numbers between start_range and end_range.
    :return: tuple(int, int)
    """
    while True:
        start_range = input("Enter the start of the range: ")
        try:
            start_range = int(start_range)
        except ValueError:
            print('ValueError: The input value has to be number! ')
        else:
            break

    while True:
        end_range = input("Enter the end of the range: ")
        try:
            end_range = int(end_range)
        except ValueError:
            print('ValueError: The input value has to be number! ')
        else:
            break
    return start_range, end_range
