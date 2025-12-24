import logging
from load_csv import get_csv_data
from cash import get_cash_data, update_cash_data
logger = logging.getLogger(__name__)

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename='log.txt', encoding='utf-8', level=logging.DEBUG)

google_data = get_csv_data()
print('ALL ROWS: ', google_data)
logger.info(f'ALL ROWS: {google_data}')

cash = get_cash_data()

diff = [x for x in google_data if x not in cash]

update_cash_data(diff)
print('NEW ROWS: ', diff)
logger.info(f'NEW ROWS: {diff}')
