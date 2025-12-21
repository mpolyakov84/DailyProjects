import gspread

def get_csv_data():
    gc = gspread.service_account()

    spreadsheet = gc.open('py_survey_responses')
    worksheet1 = spreadsheet.worksheet('Sheet1')

    data = worksheet1.get_all_records()
    return data