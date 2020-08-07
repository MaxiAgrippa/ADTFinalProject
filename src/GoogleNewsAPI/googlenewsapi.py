from GoogleNews import GoogleNews
import datetime
today = datetime.date.today()


class GoogleNewsMethods():
    
    # Creates a googlenews object
    def __init__(self):    
        self.googlenews = GoogleNews(lang="en")

    # This will return a list of news for perticular stock on a given date 
    def newscollection(self, stock, date):
        self.googlenews.search(stock)
        self.newsList = self.googlenews.result()
        return(self.newsList)

if __name__ == "__main__":
    news = GoogleNewsMethods()
    output = news.newscollection("APPL", today)
    #print(today)
    print(output)