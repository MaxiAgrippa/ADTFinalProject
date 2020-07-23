from src.YahooFinanceAPIManager.yahoo_finance_API_authentication import *


class YahooFinanceAPIManager:
    def __init__(self):
        """
        Constructor
        """
        self._authenticator = YahooFinanceAPIAuthentication()  # Get authenticatior
        self._authentication = self._authenticator.get_Authentication()  # Get authentication to access API
        self._jsonResult = None  # result object
        self._get_historical_data_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"

    def get_stock_historical_price(self, frequency="1d", filter="history", period1="1595298982", period2="1595385383",
                                   symbol="APPL"):
        """
        get stock historical price
        :param frequency: how frequent the data is. Allow one of following : 1d|1wk|1mo
        :param filter: Allow one of following : history|div|split TODO: what's that for/means? Currently using history.
        :param period1: record start time
        :param period2: record end time
        :param symbol: The company symbol, for example Microsoft: MSFT
        :return: result object, you can get the content by access result.text(it's a json file string)
        """
        querystring = {"frequency": frequency, "filter": filter, "period1": period1, "period2": period2, "symbol": symbol}
        result = requests.request("GET", self._get_historical_data_url, headers=self._authentication,
                                  params=querystring)
        return result


def main():
    """
    require 2 day of stock history price data to test.
    """
    yfapim = YahooFinanceAPIManager()
    result = yfapim.get_stock_historical_price("1d", "history", "1595126182", "1595385382", "GOOGL")
    print(result.text)


if __name__ == '__main__':
    main()
