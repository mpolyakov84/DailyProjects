import gspread


def get_csv_data():
    """
    Function to get data from Google Sheet
    :return: list of data
    """
    gc = gspread.service_account()

    spreadsheet = gc.open('py_survey_responses')
    worksheet1 = spreadsheet.worksheet('Sheet1')

    data = worksheet1.get_all_values()
    return data
