# App write and read to CSV contacts
import csv
#TODO - logging


def csv_writer(data):
    with open('contacts.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['name', 'telephone', 'email'])
        writer.writerow(data)
        print('Contact saved')


def csv_reader():
    with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)
        return list(data)


def user_interaction():
    print('Welcome to contact book')
    name = input("Enter name: ")
    telephone = input("Enter phone number: ")
    email = input("Enter email: ")
    csv_writer([name, telephone, email])

    get_contact_input = input("View all contacts? ")
    if get_contact_input in ['yes', 'y']:
        data = csv_reader()
        print(f'{data[0][0].capitalize()}: {data[1][0]} \n{data[0][1].capitalize()}: '
              f'{data[1][1]} \n{data[0][2].capitalize()}: {data[1][2]}')
    else:
        print('Bye')
