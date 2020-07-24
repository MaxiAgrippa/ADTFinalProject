from src.YahooFinanceAPIManager.YahooFinanceAPIManager import *
from src.MongoDBAtlasAPI.MongoDBAtlasAPIManager import *
import json


class StockPriceDataCollector:
    def __init__(self):
        """
        Constructor
        """
        self._mongodb_atlas_api_manager = MongoDBAtlasAPIManager()  # get MongoDB Atlas API Manager
        self._yahoo_finance_api_manager = YahooFinanceAPIManager()  # get Yahoo Finance API Manager

    # FIXME: only support one company, need to make it support multiple tables.
    def initial_add_stock_price_data(self, frequency, data_filter, start_period, end_period, company_symbol):
        # rename Yahoo Finance API Manager
        yfapim = self._yahoo_finance_api_manager
        # request stock prices data
        result = yfapim.get_stock_historical_price(frequency, data_filter, start_period, end_period, company_symbol)
        # store the extracted data
        data = {"prices": [], "id": 0, "companySymbol": company_symbol, "timeZone": {"gmtOffset": 0}}
        # check if the request result is empty or not
        if result.text is not None:
            # transform the data to json object
            json_obj = json.loads(result.text)
            # copy id from the original data
            data["id"] = json_obj["id"]
            # copy timeZone from the original data
            data["timeZone"] = json_obj["timeZone"]
            # copy part of prices from the original data
            for price in json_obj["prices"]:
                # only use date, open, close, and volume from the original data
                price_unit = {"date": price["date"], "open": price["open"], "close": price["close"], "volume": price[
                    "volume"]}
                data["prices"].append(price_unit)
            # TEST:
            print(data)

        else:
            print("Yahoo Finance API Manager request result is Empty.")


def main():
    spdc = StockPriceDataCollector()
    spdc.add_stock_price_data("1d", "history", "1595126182", "1595385382", "GOOGL")


if __name__ == '__main__':
    main()
