# app count how many numbers from 1 to 100 are divisible by 3 and 5 with Python

def divisible_3and5(n):
    """
    Func return the divisible by both 3 and 5 number
    :param n: integer
    :return: list of divisible numbers
    """
    result_list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result_list.append(i)

    return result_list


result = divisible_3and5(100)
print(f'Number from 1 to 100 divisible by both 3 and 5: \n{result} \nTotal count: {len(result)}')
