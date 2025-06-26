# App counts how many times a number appears in a list
norm_list = []
while True:
    next_step = False
    input_numbers = input("Enter a list of numbers separated by a commas: ")
    input_numbers = input_numbers.split(",")
    norm_list_tmp = [item.strip() for item in input_numbers]
    norm_list = []
    for num in norm_list_tmp:
        try:
            num = int(num)
            norm_list.append(num)
        except ValueError:
            print("Error: all inputs have to be number. Please try again.")
            next_step = True
            break
    if not next_step:
        break

while True:
    chosen_number = input('Enter the number what you want to count: ')
    if chosen_number.isdigit():
        chosen_number = int(chosen_number)
        break
    else:
        print("Error: entered value has to be number. Please try again.")

counter = 0
for num in norm_list:
    if num == chosen_number:
        counter += 1

# print(norm_list, chosen_number, counter)
print(f'The number {chosen_number} appears {counter} times in the list. ')
