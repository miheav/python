import requests;
from decimal import *
from datetime import datetime
getcontext().prec = 4

def currency_rates(code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text


    code = code.upper()

    if code not in response:
        return None

    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)


    response = response[response.find(code):]
    response = response[:response.find('</Value>')]
    rub = response[response.find('<Value>') + 7:]


    return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"