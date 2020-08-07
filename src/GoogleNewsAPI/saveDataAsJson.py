from googlenewsapi import GoogleNewsMethods
import pandas as pd
import datetime 
import json

# This is to get current date.
today = datetime.date.today()


# This class is to store the data that is retrived from GoogleNewsAPI to save it as Json file.
class JsonOperations():
    # Initializing pandas dataframe.
    def __init__(self,dataInput):
        self.dataInput = pd.DataFrame(dataInput)
    # Saving the data in data.json.
    def saveAsJson(self):
        jsonData = self.dataInput.to_json(orient="table")
        parsed = json.loads(jsonData)
        with open('data.json', 'w') as outfile:
            json.dump(parsed,outfile,indent=4)
    # printting data that is stored on console.
    def displayPdData(self):
        print(self.dataInput.columns)
        self.dataInput['companyName'] = 'APPL'
        for index, row in self.dataInput.iterrows():
            print(row.to_json())        


if __name__ == "__main__":
    news = GoogleNewsMethods()
    op = JsonOperations(news.newscollection("APPL",today))
    op.saveAsJson()
    op.displayPdData()
    