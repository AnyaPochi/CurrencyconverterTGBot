import requests
import json
from config import keys
class APIException(Exception):
    pass

class Get_Price:
    @staticmethod
    def convert(quote: str, base: str, amount :str ):
        if quote == base:
            raise APIException('Валюты идентичны, конвертировать нечего')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось найти валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось найти валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        r = requests.get('https://v6.exchangerate-api.com/v6/df98dfeb3f2ca5f81cf59a89/latest/USD')
        cur_cor =json.loads(r.content)['conversion_rates']
        total_base = cur_cor[quote_ticker]*(amount/cur_cor[base_ticker])
        return total_base