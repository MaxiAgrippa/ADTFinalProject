from pymongo import MongoClient


class MongoDBAtlasAPIAuthentication:

    def __init__(self):
        """
        Constructor
        provide information to connect mongoDB Atlas
        """
        self._username = "m220student"  # username
        self._password = "m220password"  # password
        self._cluster = "mflix.8tenw.gcp.mongodb.net"  # the cluster we gonna use (maybe)
        self._database = "test"  # the database (maybe)

    def _format_connection_url(self):
        """
        format the url for the connection with mongodb
        :return: url : the url string
        """
        url = "mongodb+srv://" + self._username + ":" + self._password + "@" + self._cluster + "/" + self._database
        return url

    def get_mongodb_client(self):
        """
        connect to mongodb Atlas and return the connection object
        :return: client the connection object with mongodb Atlas
        """
        try:
            client = MongoClient(self._format_connection_url())
        except Exception as e:
            print(e)
        return client


def main():
    """
    requre the state of the database.
    """
    # TEST test head SUCCESS
    mdbaa = MongoDBAtlasAPIAuthentication()
    client = mdbaa.get_mongodb_client()
    # print client state
    print(client.state)


if __name__ == '__main__':
    main()
