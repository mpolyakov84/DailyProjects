from sum_numbers import sum_numbers, usr_interaction

num_range = usr_interaction()
nums = sum_numbers(num_range)
print(f'The sum of all numbers from {num_range[0]} to {num_range[1]} is: {nums}')
