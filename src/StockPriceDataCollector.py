from src.YahooFinanceAPIManager.YahooFinanceAPIManager import *
from src.MongoDBAtlasAPI.MongoDBAtlasAPIManager import *
from datetime import datetime
import time
import json


class StockPriceDataCollector:
    def __init__(self):
        """
        Constructor
        """
        self._mongodb_atlas_api_manager = MongoDBAtlasAPIManager()  # get MongoDB Atlas API Manager
        self._yahoo_finance_api_manager = YahooFinanceAPIManager()  # get Yahoo Finance API Manager

    def add_stock_price_data(self, start_period, end_period, company_symbol, frequency="1d", data_filter="history"):
        """
        Add stock price data of a company in a period of time(epoch time) to the database
        :param frequency: the time interval between each data unit. ()
        :param data_filter: Allow one of following : history|div|split TODO: what's that for/means? Currently using history.
        :param start_period: record start time
        :param end_period: record end time
        :param company_symbol: The company symbol, for example Microsoft: MSFT
        :return: -1 indicate something wrong, 0 indicate normal
        """
        # rename Yahoo Finance API Manager
        yfapim = self._yahoo_finance_api_manager
        # rename MongoDB Atlas API Manager
        mdbaapim = self._mongodb_atlas_api_manager
        # request stock prices data
        result = yfapim.get_stock_historical_price(frequency, data_filter, start_period, end_period, company_symbol)
        # store the data units for insertion
        datas = []
        # check if the request result is empty or not
        if result.text is not None:
            # transform the data to json object
            json_obj = json.loads(result.text)
            # copy part of prices from the original data
            for price in json_obj["prices"]:
                if "open" in price:
                    # store the extracted data for each data unit
                    data = {"date": price["date"], "open": price["open"], "close": price["close"], "volume": price[
                        "volume"], "companySymbol": company_symbol, "timeZone": json_obj["timeZone"]}
                    # append the data unit to datas array for insert many data in one time.
                    datas.append(data)
            # TEST:
            # print(datas)
            # insert datas to the collection.
            try:
                mdbaapim.store_stock_price_data(company_symbol, datas)
                # if something goes wrong with mongoDB Atlas, print the error.
            except Exception as e:
                print(e)
                return -1
        else:
            # If the there is no data from Yahoo Finance API Manager, show an error.
            print("Yahoo Finance API Manager request result is Empty.")
            return -1
        return 0

    def add_financial_data(self, region, company_symbol):
        """
        Add financial data of a company to the database
        :param region: the region for which the data is collected
        :param company_symbol: The company symbol, for example Microsoft: MSFT
        :return: -1 indicate something wrong, 0 indicate normal
        """
        # rename Yahoo Finance API Manager
        yfapim = self._yahoo_finance_api_manager
        # rename MongoDB Atlas API Manager
        mdbaapim = self._mongodb_atlas_api_manager
        # request stock prices data
        result = yfapim.get_summary(region, company_symbol)
        # store the data units for insertion
        data_set = []
        # check if the request result is empty or not
        if result.text is not None:
            # transform the data to json object
            json_obj = json.loads(result.text)
            # get the date in epoch format
            today = datetime.today().strftime('%s')
            # TEST: date and epoch conversions: SUCCESS
            print(today)
            print("\n")
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(today))))
            print("\n")
            # populate the data object
            data = {"symbol": company_symbol,
                    "date": today,
                    "earnings": json_obj["earnings"],
                    "recommendationTrend": json_obj["recommendationTrend"]}
            # add object to an array
            data_set.append(data)
            # insert data_set to the collection.
            try:
                mdbaapim.store_financial_data(data_set)
                # if something goes wrong with mongoDB Atlas, print the error.
            except Exception as e:
                print(e)
                return -1
        else:
            # If the there is no data from Yahoo Finance API Manager, show an error.
            print("Yahoo Finance API Manager request result is Empty.")
            return -1
        return 0

    def search_stock_price_data(self, start_period, end_period, company_symbol):
        """
        search in the company_symbol collection for stock price data,
        the time range is between start_period and end_period.
        :param start_period: the begin time of the date range
        :param end_period: the end time of the date range
        :param company_symbol: company symbol indicate which company, eg. "MSFT"
        :return: result from the client or None if something is wrong.
        """
        # rename MongoDB Atlas API Manager
        mdbaapim = self._mongodb_atlas_api_manager
        # if start_period is smaller than end_period, show an message and return None.
        if start_period > end_period:
            print("ERROR(search_stock_price_data()): start period is bigger than end period!")
            return None
        # build json_filter to search the data.
        json_filter = {"date": {"$gte": start_period, "$lte": end_period}, "companySymbol": company_symbol}
        # search the company_symbol collection.
        try:
            result = mdbaapim.search_stock_price_data(company_symbol, json_filter=json_filter)
            # if something goes wrong, print the error and return None
        except Exception as e:
            print(e)
            return None
        return result

    def search_stock_price_data_advance(self, start_period, end_period, company_symbol, json_projection=None):
        """
        search in the company_symbol collection for stock price data,
        the time range is between start_period and end_period.
        only show result according to the json_projection requirement.
        :param start_period: the begin time of the date range
        :param end_period: the end time of the date range
        :param company_symbol: company symbol indicate which company, eg. "MSFT"
        :param json_projection: Optional, the rules to select property from the result set.
        :return: result from the client or None if something is wrong.
        """
        # rename MongoDB Atlas API Manager
        mdbaapim = self._mongodb_atlas_api_manager
        # if start_period is smaller than end_period, show an message and return None.
        if start_period > end_period:
            print("ERROR(search_stock_price_data()): start period is bigger than end period!")
            return None
        # build json_filter to search the data.
        json_filter = {"date": {"$gte": start_period, "$lte": end_period}, "companySymbol": company_symbol}
        # search the company_symbol collection.
        try:
            result = mdbaapim.search_stock_price_data(company_symbol, json_filter=json_filter,
                                                      json_projection=json_projection)
            # if something goes wrong, print the error and return None
        except Exception as e:
            print(e)
            return None
        return result


def main():
    # TEST: request and store stock price data for one company: SUCCESS
    spdc = StockPriceDataCollector()
    # TEST: add financial data to a new collection in MongoDB: SUCCESS
    # spdc.add_financial_data("US", "AAPL")

    # the order is: start_period, end_period, company_symbol, frequency="1d", data_filter="history"
    # spdc.add_stock_price_data("0", "1596651732", "DIS", "1d", "history")

    # TEST: search stock price data for one company: SUCCESS
    # result = spdc.search_stock_price_data(1595856600, 1595856600, "GOOGL")
    # print(result)
    # for r in result:
    #     if r is not None:
    #         print(r)
    # result2 = spdc.search_stock_price_data(1595856500, 1595856700, "GOOGL")
    # print(result2)
    # for r in result2:
    #     if r is not None:
    #         print(r)
    # result3 = spdc.search_stock_price_data(1595856700, 1595856500, "GOOGL")
    # print(result3)
    # if result3 is not None:
    #     for r in result3:
    #         if r is not None:
    #             print(r)

    # TEST: search stock price data advance for one company: SUCCESS
    # result4 = spdc.search_stock_price_data_advance(1595856500, 1595856700, "GOOGL", {"_id": 0})
    # print(result4)
    # if result4 is not None:
    #     for r in result4:
    #         if r is not None:
    #             print(r)


if __name__ == '__main__':
    main()
