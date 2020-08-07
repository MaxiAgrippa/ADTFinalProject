import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import datetime
import time
from GoogleNewsAPI.googlenewsapi import GoogleNewsMethods
import pandas as pd
from MongoDBAtlasAPI.MongoDBAtlasAPIAuthentication import MongoDBAtlasAPIAuthentication
from GoogleNewsAPI.NewsMongoDBOperations import NewsMongoDBOperations

class RetrivingStockInfo():
    def __init__(self):
        self.news = GoogleNewsMethods()
        self.mdbaa = MongoDBAtlasAPIAuthentication()
        self.client = self.mdbaa.get_mongodb_client()
        # print client state
        self.db=self.client.StockMarket
        self.collection_names = self.db.list_collection_names()
        self.mongodbNewsOperations = NewsMongoDBOperations()
    
    def intratingThroughdata(self):
        for col_num, col in enumerate(self.collection_names):
            if(col=='GOOGL'):
                self.collection=self.db[col]
                self.cursor = self.collection.find({},{"_id":0,"companySymbol":1,"date":1})
                count =0
                for document in self.cursor:
                    dateForOneDoc = int(document.get('date'))
                    companySymbol = document.get('companySymbol')
                    if (dateForOneDoc != None):
                        formatedDate = datetime.datetime.fromtimestamp(dateForOneDoc).strftime('%Y-%m-%d')
                        newsList = self.news.newscollection(companySymbol,formatedDate)

                        data = pd.DataFrame(newsList)

                        data['companyName'] = companySymbol
                        for index, row in data.iterrows():
                            if(self.mongodbNewsOperations.checkForDuplication(row, formatedDate)):
                                print("news added")


if __name__ == "__main__":
     addData = RetrivingStockInfo()
     addData.intratingThroughdata()