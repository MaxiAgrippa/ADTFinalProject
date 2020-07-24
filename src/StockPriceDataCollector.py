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

    def initial_add_stock_price_data(self, frequency, data_filter, start_period, end_period, company_symbol):
        # rename Yahoo Finance API Manager
        yfapim = self._yahoo_finance_api_manager
        # rename MongoDB Atlas API Manager
        mdbaapim = self._mongodb_atlas_api_manager
        # request stock prices data
        result = yfapim.get_stock_historical_price(frequency, data_filter, start_period, end_period, company_symbol)
        # store the extracted data for the first insert
        data = {"prices": [], "id": 0, "companySymbol": company_symbol, "timeZone": {"gmtOffset": 0}}
        # check if the request result is empty or not
        if result.text is not None:
            # transform the data to json object
            json_obj = json.loads(result.text)
            if mdbaapim.check_stock_price_data_existence(company_symbol) is False:
                # copy id from the original data
                data["id"] = json_obj["id"]
                # copy timeZone from the original data
                data["timeZone"] = json_obj["timeZone"]
                # copy part of prices from the original data
                for price in json_obj["prices"]:
                    # form a price unit only use date, open, close, and volume from the original data
                    price_unit = {"date": price["date"], "open": price["open"], "close": price["close"], "volume":
                        price["volume"]}
                    # store the price unit into "prices" object.
                    data["prices"].append(price_unit)
                # TEST:
                print(data)
                # using data to create the document.
                mdbaapim.initial_store_stock_price_data(company_symbol, data)
            else:
                # store the extracted data for update the price part
                price_data = {"prices": {"$each": []}}
                # copy part of prices from the original data
                for price in json_obj["prices"]:
                    price_unit = {"date": price["date"], "open": price["open"], "close": price["close"], "volume":
                        price["volume"]}
                    # store the price unit into "prices" object.
                    price_data["prices"]["$each"].append(price_unit)
                # TEST:
                print(price_data)
                # using price_data to update the "prices" part
                # FIXME: need a way to avoid duplication.
                mdbaapim.add_data_stock_price_data(company_symbol, price_data)
                # TODO: TO BE CONTINUE:



        else:
            print("Yahoo Finance API Manager request result is Empty.")


def main():
    spdc = StockPriceDataCollector()
    spdc.initial_add_stock_price_data("1d", "history", "1595126182", "1595385382", "GOOGL")


if __name__ == '__main__':
    main()
