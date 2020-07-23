# for test
import requests


class YahooFinanceAPIAuthentication:

    def __init__(self):
        """
        Constructor
        """
        # this is the host key pair for Authentication,
        # if my limit is reached, switch the below part.
        self.__headers__ = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "c2829536e9msh4b1be8fae335bf0p141362jsnc364d462c0ad"
        }

    def get_Authentication(self):
        """
        get Authentication
        :return: __headers__ the host and key for Authentication
        """
        return self.__headers__


def main():
    """
    require 1 day of stock history price data to test.
    """
    # TEST test head SUCCESS
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"

    yfapia = YahooFinanceAPIAuthentication()

    querystring = {"frequency": "1d", "filter": "history", "period1": "1595298982", "period2": "1595385383", "symbol": "MSFT"}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "c2829536e9msh4b1be8fae335bf0p141362jsnc364d462c0ad"
    }

    response = requests.request("GET", url, headers=yfapia.get_Authentication(), params=querystring)

    print(response.text)


if __name__ == '__main__':
    main()
