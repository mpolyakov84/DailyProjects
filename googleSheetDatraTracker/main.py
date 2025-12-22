from load_csv import get_csv_data
from cash import get_cash_data, update_cash_data

google_data = get_csv_data()
print('ALL ROWS: ', google_data)

cash = get_cash_data()

diff = [x for x in google_data if x not in cash]

update_cash_data(diff)
print('NEW ROWS: ', diff)
