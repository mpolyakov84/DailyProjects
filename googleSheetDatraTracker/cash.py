from pathlib import Path
import csv

cash_path = Path('cash.txt')

# if not cash_path.exists():
#     cash_path.touch()
#     print('Cash file has been created')

try:
    cash_path.touch(exist_ok=False)
except FileExistsError:
    print('Cash file already exists')
else:
    print('Cash file has been created')

# write with join
# with open(cash_path, 'a+') as file:
#     for row in data:
#         file.write(', '.join(row))
#         file.write('\n')


def update_cash_data(data):
    """
    Update data in cash file
    :param data: list of data from gsheet
    :return: save data in file
    """
    with open(cash_path, 'a+') as file:
        csv_writer = csv.writer(file, lineterminator='\n')

        for row in data:
            csv_writer.writerow(row)


def get_cash_data():
    """
    get cash data from cash.txt file
    :return:
    """
    with open(cash_path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        lst = []
        for row in reader:
            lst.append(row)
    return lst
