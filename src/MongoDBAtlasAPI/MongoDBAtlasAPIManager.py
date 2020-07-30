from src.MongoDBAtlasAPI.MongoDBAtlasAPIAuthentication import *
import pprint


class MongoDBAtlasAPIManager:

    def __init__(self):
        """
        Constructor
        """
        self._authenticator = MongoDBAtlasAPIAuthentication()  # Get authenticatior
        self._authentication = self._authenticator.get_mongodb_client()  # Get authentication to access API

    def get_state(self):
        """
        get data connection state.
        :return: data connection state
        """
        return self._authentication.state

    def store_stock_price_data(self, company_symbol, json_data_array):
        """
        used in store data.
        :param company_symbol: the company(table) you want to initialize
        :param json_data_array: json data array(document array)
        :return: result: the result from connection object.
        """
        # rename the authentication
        client = self._authentication
        try:
            # insert many document object, automatically set _id as default.
            # connection.database.collection.function()
            result = client.StockMarket[company_symbol].insert_many(json_data_array)
        except Exception as e:
            print(e)
        return result

    def search_stock_price_data(self, company_symbol, json_filter=None, json_projection=None):
        """
        search in a company's collection for stock price data
        :param company_symbol: the collection name also the company symbol
        :param json_filter: a SON object specifying elements which must be present for a document to be included in the result set
        :param json_projection: a list of field names that should be returned in the result set or a dict specifying the fields to include or exclude.
        :return: result: the result from connection object.
        """
        # rename the authentication
        client = self._authentication
        try:
            # find document objects inside the company collection.
            # connection.database.collection.function()
            result = client.StockMarket[company_symbol].find(json_filter, json_projection)
        except Exception as e:
            print(e)
        return result

    def drop_stock_price_data(self, company_symbol):
        """
        drop the StockPrice table(?)
        :param company_symbol: the company(table) you want to drop
        """
        # rename the authentication
        client = self._authentication
        try:
            # drop that company collection.
            client.StockMarket[company_symbol].drop()
        except Exception as e:
            print(e)

    # FIXME: delete duplicated data
    # OLD: ERROR for now
    # FIXME: Useless?
    def add_data_stock_price_data(self, company_symbol, json_data_array):
        """
        add data to StockPrice
        :param company_symbol: the company(table) you want to add price data to
        :param json_data_array: json format data that gonna add to the document
        :return: result: the result from connection object.
        """
        # rename the authentication
        client = self._authentication
        try:
            if self.check_stock_price_data_existence(company_symbol):
                # need to use "$each" in the json_data_array to add multiple values to the array field.
                result = client.StockMarket[company_symbol].update_many({}, {"$addToSet": json_data_array})
                # TODO:
                # delete duplicated data
                pipline = {}
                client.StockMarket[company_symbol].aggregate(pipline)
            else:
                print("Empty collection.")
        except Exception as e:
            print(e)
        return result

    def check_stock_price_data_existence(self, company_symbol):
        """
        Check if there is any data?
        :param company_symbol: the company(table) you want to check.
        :return: True for has data, False for empty
        """
        # rename the authentication
        client = self._authentication
        result = client.StockMarket[company_symbol].find_one({})
        if result is not None:
            return True
        return False


def main():
    mdbaapim = MongoDBAtlasAPIManager()
    # TEST: Connection SUCCESS
    print(mdbaapim.get_state())

    # TEST: Initial insert data SUCCESS:
    # result = mdbaapim.store_stock_price_data("test", [
    #     {"date": 20200724, "open": 1.2, "close": 2.3, "volume": 1000, "companySymbol": "test", "timeZone": {"gmtOffset": -14400}},
    #     {"date": 20200725, "open": 2.2, "close": 3.3, "volume": 1001, "companySymbol": "test", "timeZone": {"gmtOffset": -14400}},
    #     {"date": 20200726, "open": 3.2, "close": 4.3, "volume": 1002, "companySymbol": "test", "timeZone": {"gmtOffset": -14400}},
    # ])
    # print(result)

    # TEST: drop. SUCCESS
    # print(mdbaapim.drop_stock_price_data("test"))

    # FIXME: useless?
    # TEST: add data ERROR
    # need to use "$each" with the parameters to add multiple values to the array field.
    # result2 = mdbaapim.add_data_stock_price_data("test",
    #                                              {"prices": {"$each": [
    #                                                  {"data": 20200725, "open": 2.2, "close": 3.3, "volume": 1000},
    #                                                  {"data": 20200726, "open": 3.2, "close": 4.3, "volume": 1000}]}})
    # print(result2)

    # TEST: check data existence. SUCCESS
    # if mdbaapim.check_stock_price_data_existence("test"):
    #     print("E")
    # else:
    #     print("N")

    # TEST: search stock price data. SUCCESS
    result3 = mdbaapim.search_stock_price_data("test", {"data": {"$gte": 20200725, "$lte": 20200726}}, {"_id": 0})
    for r in result3:
        print(r)


if __name__ == '__main__':
    main()
