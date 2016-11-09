from decimal import Decimal
from HTMLParser import HTMLParser

import requests

from preferences import preferences


class CustomHTMLParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        self.stop = False
        HTMLParser.__init__(self, *args, **kwargs)

    def handle_starttag(self, tag, attrs):
        if attrs:
            if attrs[0][1] == 'price':
                self.stop = True
            else:
                self.stop = False
        else:
            self.stop = False

    def handle_data(self, data):
        if self.stop:
            data = data.strip()
            stock_ticker = preferences.SitePreferences.active_stock_ticker
            stock_ticker.previous_stock_value = stock_ticker.current_stock_value
            stock_ticker.current_stock_value = Decimal(data)
            stock_ticker.save()


def get_latest_stock_value():
    response = requests.get(
        'http://www.bloomberg.com/quote/GUINNESS:NL'
    )

    parser = CustomHTMLParser()
    parser.feed(response.text)
