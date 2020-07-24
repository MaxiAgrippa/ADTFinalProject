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


def main():
    mdbaapim = MongoDBAtlasAPIManager()
    # TEST: Connection SUCCESS
    print(mdbaapim.get_state())
    # TEST: Insert data SUCCESS
    result = mdbaapim.initial_store_stock_price_data([{"A": 1.2, "B": 2.3}])
    print(result)


if __name__ == '__main__':
    main()
