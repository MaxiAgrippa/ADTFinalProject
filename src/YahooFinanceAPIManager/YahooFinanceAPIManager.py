from src.YahooFinanceAPIManager.YahooFinanceAPIAuthentication import *
# TEST: using json.loads to convert the string result to a json style. SUCCESS
import json


class YahooFinanceAPIManager:
    def __init__(self):
        """
        Constructor
        """
        self._authenticator = YahooFinanceAPIAuthentication()  # Get authenticatior
        self._authentication = self._authenticator.get_Authentication()  # Get authentication to access API
        self._jsonResult = None  # result object
        self._get_historical_data_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"
        self._get_financials_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
        self._get_summary_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

    def get_stock_historical_price(self, frequency="1d", data_filter="history", period1="1595298982", period2="1595385383",
                                   symbol="APPL"):
        """
        get stock historical price of a company
        :param frequency: how frequent the data is. Allow one of following : 1d|1wk|1mo
        :param data_filter: Allow one of following : history|div|split TODO: what's that for/means? Currently using history.
        :param period1: record start time
        :param period2: record end time
        :param symbol: The company symbol, for example Microsoft: MSFT
        :return: result object, you can get the content by access result.text(it's a json file string)
        """
        # construct query json string
        querystring = {"frequency": frequency, "filter": data_filter, "period1": period1, "period2": period2, "symbol": symbol}
        # query and store result
        result = requests.request("GET", self._get_historical_data_url, headers=self._authentication,
                                  params=querystring)
        return result

    def get_financials(self, symbol="AAPL"):
        """
        get financial states of a company
        :param symbol: The company symbol, for example Microsoft: MSFT
        :return: result object, you can get the content by access result.text(it's a json file string)
        """
        # construct query json string
        querystring = {"symbol": symbol}
        # query and store result
        result = requests.request("GET", self._get_financials_url, headers=self._authentication,
                                  params=querystring)
        return result

    def get_summary(self, region="US", symbol="AAPL"):
        """
        get financial summary of a company
        :param region: the region for which the summary is retrieved
        :param symbol: the company symbol, for example Microsoft: MSFT
        :return: result object, you can get the content by access result.text(it's a json file string)
        """
        # construct query json string
        querystring = {"region": region, "symbol": symbol}
        # query and store result
        result = requests.request("GET", self._get_summary_url, headers=self._authentication,
                                  params=querystring)
        return result


def main():
    """
    require 2 day of stock history price data to test.
    """
    # TEST: getting 2 days of google stock price data and google's financial state. SUCCESS
    yfapim = YahooFinanceAPIManager()
    result = yfapim.get_stock_historical_price("1d", "history", "1595126182", "1595385382", "GOOGL")
    result2 = yfapim.get_financials("GOOGL")
    result_summary = yfapim.get_summary("US", "AAPL")
    print(result.text)
    print("\n")
    # TEST: using json.loads to convert the string result to a json style. SUCCESS
    json_obj = json.loads(result.text)
    print(json_obj["prices"])
    print("\n")
    # print(result2.text)
    # print("\n")
    # print(result_summary.text)
    json_summary = json.loads(result_summary.text)
    print(json_summary["recommendationTrend"])
    print("\n")
    print(json_summary["earnings"])
    print("\n")
    print(json_summary["financialData"])


if __name__ == '__main__':
    main()
