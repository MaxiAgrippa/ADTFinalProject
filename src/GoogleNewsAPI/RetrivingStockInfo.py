import sys
sys.path.insert(1, 'D:\Sync\Advanced Database Topics\FinalProject\Max Repo\ADTFinalProject\src\MongoDBAtlasAPI')
import pandas as pd
import datetime
import time

from MongoDBAtlasAPIAuthentication import MongoDBAtlasAPIAuthentication

if __name__ == "__main__":
    mdbaa = MongoDBAtlasAPIAuthentication()
    client = mdbaa.get_mongodb_client()
    # print client state
    db=client.StockMarket
    collection_names = db.list_collection_names() 
    for col_num, col in enumerate(collection_names):
            collection=db[col]
            cursor = collection.find({},{"_id":0,"companySymbol":1,"date":1})
            count =0
            for document in cursor:
                dateForOneDoc = document.get('date')
                if (dateForOneDoc != None):
                    #print(document.get('companySymbol'))
                    formatedDate = datetime.datetime.fromtimestamp(dateForOneDoc).strftime('%c') 
                    print(formatedDate)
                                                        
                
            print(count)