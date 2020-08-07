import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from GoogleNewsAPI.googlenewsapi import GoogleNewsMethods
from MongoDBAtlasAPI.MongoDBAtlasAPIAuthentication import MongoDBAtlasAPIAuthentication
import datetime
today = datetime.date.today()
class NewsMongoDBOperations():

    def __init__(self):
        self._authenticator = MongoDBAtlasAPIAuthentication()  # Get authenticatior
        self._authentication = self._authenticator.get_mongodb_client()  # Get authentication to access API
        
    def checkForDuplication(self, data,date):
        if ('hours' in data['date']):
            data['date']= date
            companyName = data['companyName']
            client = self._authentication
            myquery = {"title":data['title']}
            condition = client.StockDataNews[companyName].find(myquery).limit(1).count()
            if (condition==0):
                self.saveToMongoDB(data)
                return 1 
            else:    
                return 0
    def saveToMongoDB(self,data):
        client = self._authentication
        try:
            # insert many document object, automatically set _id as default.
            # connection.database.collection.function()
            result = client.StockDataNews[data['companyName']].insert_one(data.to_dict())
        except Exception as e:
            print(e)
        return 0
    def get_state(self):
        """
        get data connection state.
        :return: data connection state
        """
        return self._authentication.state
if __name__ == "__main__":
    object =  NewsMongoDBOperations()
    data = {
            "index": 1,
            "title": "Apple Smashes Revenue, iPhone Estimates in Record Third Quarter",
            "media": "Bloomberg",
            "date": "6 hours ago",
            "desc": "Apple Inc. reported quarterly revenue that crushed Wall Street forecasts after locked down consumers snapped up new iPhones, iPads and ...",
            "link": "https://www.bloomberg.com/news/articles/2020-07-30/apple-smashes-revenue-iphone-estimates-in-record-third-quarter",
            "img": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
            "companyName": "GOOGL"
        }
    date = today
    object.checkForDuplication(data,date)