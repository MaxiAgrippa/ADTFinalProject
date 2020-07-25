from src.MongoDBAtlasAPI.MongoDBAtlasAPIAuthentication import *


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

    # TEST TEMPORARY METHOD, not decided.
    def initial_store_stock_price_data(self, company, json_data_array):
        """
        used in store data for the first time.
        :param company: the company(table) you want to initialize
        :param json_data_array: json data array(document array)
        :return: result: the result from connection object.
        """
        # rename the authentication
        client = self._authentication
        try:
            # insert many document object, automatically set _id as default.
            # connection.database.collection.function()
            result = client.StockMarket[company].insert_many(json_data_array)
        except Exception as e:
            print(e)
        return result

    def drop_stock_price_data(self, company):
        """
        drop the StockPrice table(?)
        :param company: the company(table) you want to drop
        """
        # rename the authentication
        client = self._authentication
        try:
            result = client.StockMarket[company].drop()
        except Exception as e:
            print(e)

    # FIXME: delete duplicated data
    def add_data_stock_price_data(self, company, json_data_array):
        """
        add data to StockPrice
        :param company: the company(table) you want to add price data to
        :param json_data_array: json format data that gonna add to the document
        :return: result: the result from connection object.
        """
        # rename the authentication
        client = self._authentication
        try:
            if self.check_stock_price_data_existence(company):
                # need to use "$each" in the json_data_array to add multiple values to the array field.
                result = client.StockMarket[company].update_many({}, {"$addToSet": json_data_array})
                # TODO:
                # delete duplicated data
                pipline = {}
                client.StockMarket[company].aggregate(pipline)
            else:
                print("Empty collection.")
        except Exception as e:
            print(e)
        return result

    def check_stock_price_data_existence(self, company):
        """
        Check if there is any data?
        :param company: the company(table) you want to check.
        :return: True for has data, False for empty
        """
        # rename the authentication
        client = self._authentication
        result = client.StockMarket[company].find_one({})
        if result is not None:
            return True
        return False


def main():
    mdbaapim = MongoDBAtlasAPIManager()
    # TEST: Connection SUCCESS
    print(mdbaapim.get_state())
    # TEST: Initial insert data SUCCESS
    # result = mdbaapim.initial_store_stock_price_data("test", [{"prices": [
    #     {"data": 20200724, "open": 1.2, "close": 2.3, "volume": 1000}], "id": 111, "companySymbol": "test", "timeZone": {"gmtOffset": -14400}}])
    # print(result)
    # TEST: drop SUCCESS
    print(mdbaapim.drop_stock_price_data("test"))
    # TEST: add data SUCCESS
    # need to use "$each" with the parameters to add multiple values to the array field.
    # result2 = mdbaapim.add_data_stock_price_data("test",
    #                                              {"prices": {"$each": [
    #                                                  {"data": 20200725, "open": 2.2, "close": 3.3, "volume": 1000},
    #                                                  {"data": 20200726, "open": 3.2, "close": 4.3, "volume": 1000}]}})
    # print(result2)
    # TEST: check data existence SUCCESS
    # if mdbaapim.check_stock_price_data_existence("test"):
    #     print("E")
    # else:
    #     print("N")


if __name__ == '__main__':
    main()
