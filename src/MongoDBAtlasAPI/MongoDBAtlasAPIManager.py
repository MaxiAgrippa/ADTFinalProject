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
    # FIXME: only support one company, need to make it support multiple tables.
    def initial_store_stock_price_data(self, json_data_array):
        """
        used in store data for the first time.
        :param json_data_array: json data array(document array)
        :return: result: the result from connection object.
        """
        client = self._authentication
        try:
            # insert many document object, automatically set _id as default.
            # connection.database.collection.function()
            result = client.StockMarket.StockPrice.insert_many(json_data_array)
        except Exception as e:
            print(e)
        return result

    def drop_stock_price_data(self):
        """
        drop the StockPrice table(?)
        """
        client = self._authentication
        try:
            result = client.StockMarket.StockPrice.drop()
        except Exception as e:
            print(e)

    # FIXME: only support one company, need to make it support multiple tables.
    def add_data_stock_price_data(self, json_data_array):
        """
        add data to StockPrice
        :param json_data_array: json format data that gonna add to the document
        :return: result: the result from connection object.
        """
        client = self._authentication
        try:
            if self._check_stock_price_data_existence():
                # need to use "$each" in the json_data_array to add multiple values to the array field.
                result = client.StockMarket.StockPrice.update_many({}, {"$addToSet": json_data_array})
            else:
                print("Empty collection.")
        except Exception as e:
            print(e)
        return result

    # FIXME: only support one company, need to make it support multiple tables.
    def _check_stock_price_data_existence(self):
        """
        Check if there is any data?
        :return: True for has data, False for empty
        """
        client = self._authentication
        result = client.StockMarket.StockPrice.find_one({})
        if result is not None:
            return True
        return False


def main():
    mdbaapim = MongoDBAtlasAPIManager()
    # TEST: Connection SUCCESS
    print(mdbaapim.get_state())
    # TEST: Initial insert data SUCCESS
    result = mdbaapim.initial_store_stock_price_data([{"prices": [
        {"data": 20200724, "open": 1.2, "close": 2.3, "volume": 1000}], "id": 111, "companySymbol": "test", "timeZone": {"gmtOffset": -14400}}])
    print(result)
    # TEST: drop SUCCESS
    # print(mdbaapim.drop_stock_price_data())
    # TEST: add data SUCCESS
    # need to use "$each" with the parameters to add multiple values to the array field.
    # result2 = mdbaapim.add_data_stock_price_data(
    #     {"prices": {"$each": [{"data": 20200725, "open": 2.2, "close": 3.3, "volume": 1000},
    #                           {"data": 20200726, "open": 3.2, "close": 4.3, "volume": 1000}]}})
    # print(result2)
    # TEST: check data existence SUCCESS
    # if mdbaapim._check_stock_price_data_existence():
    #     print("E")
    # else:
    #     print("N")


if __name__ == '__main__':
    main()
