import requests
import json
from .common import parser_html_json


def get_holiday_list():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        holiday_service = requests.get(
            'https://www1.nseindia.com/global/content/market_timings_holidays/market_timings_holidays.jsp?pageName=0&dateRange=&fromDate=01-01-2022&toDate=31-12-2023&tabActive=trading&load=false',
            headers=headers).text

        for item in json.loads(parser_html_json(holiday_service)):
            # Your Save Code
            print(item)
        return json.loads(parser_html_json(holiday_service))
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))


def is_holiday(date):
    weekday = date.weekday()
    holiday_list = get_holiday_list()
    holiday = [x for x in holiday_list if x.get('Date') == date]
    if not len(holiday) and weekday < 5:
        return False
    else:
        return True