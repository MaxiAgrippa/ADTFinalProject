# Managing stock data and related companies’ news using MongoDB Atlas

# Step: modeling the database

Regarding the modeling of the database, the initial draft the group had in mind was composed of two different collections inside the MongoDB database instance: one for the stock data (quotes, volume, etc.) and another one for the news. 

The connection between the two collections would happen with the use of two different attributes or keys: the date and the company symbol (for example, the symbol for Apple in the stock market is “AAPL”). With these two attributes, it would be possible to connect the stock data for a specific company on a specific day, with the news related to that company on the same day.

But, for the sake of simplicity, since the initial idea is to work with a restricted number of companies (no more than 5), the group decided to create individual collections for each company. Each collection’s schema is made of a document that contains the stock data for a company on a particular day plus the news related to that company on that day, in the form of an array of objects (news object). In MongoDB, this procedure is known as embedding, and it can be used for a one-to-many relationship when there’s the will to keep the database simple. It’s important to mention that the size of each document is relatively small and the growth rate is expected to be low, since the model expects only one document per company, per day.

There is also the possibility of including another collection that would hold information about other technical indicators that can be useful for anyone creating an application whose goal is to predict the behavior of stocks, such as revenue, earnings and latest recommendation trends (“sell”, “buy”, “keep”, etc.). These indicators can be found in many papers and articles, e.g. http://eprints.covenantuniversity.edu.ng/4112/1/Emerging_Trend.pdf [1] or https://ieeexplore.ieee.org/abstract/document/8489208 [2].

This decision can still be changed, as there’s a discussion going on whether the schema should be composed of one collection per company, or if it would be better to have one single collection for all the companies. Also, in the future, if there’s a decision to expand the number of companies and/or increase the frequency of which the data is collected, to have many data points on a single day, this model would probably need to be reviewed and changed.

Stock data schema screenshot:

![Stock data schema](https://github.com/MaxiAgrippa/ADTFinalProject/blob/master/screenshots/stockDataSchema.png)

# Step: MongoDB Atlas setup

When it comes to MongoDB Atlas, all steps have been successfully completed. There’s a valid account, in which there’s a cluster with a database ready to receive the data from the application.

MongoDB Atlas setup screenshot:

![MongoDB Atlas setup](https://github.com/MaxiAgrippa/ADTFinalProject/blob/master/screenshots/SetupAtlas.png)

# Step: programming languages, frameworks

Among all the options that could be used in terms of the programming language to use, the team decided to use Python, since all the group members have at least the basic knowledge to work with it. Moreover, it’s a popular language that offers a lot of support to their users, not only from the official channels, but also through all the forums and tutorials that can be found online, and it also offers good support for working with the Yahoo Finance API , JSON documents and the MongoDB framework, in the form of Python libraries.

Structure of the Python application:

Stock Market part:

MongoDB part:

- There’s an utility object called MongoDBAtlasAPIAuthentication to deal with connection information, like credentials, and to provide a client object that can be used throughout the application.

- And there’s another class called MongoDBAtlasAPIManager that is responsible for CRUD operations against the MongoDB Atlas instance.

Application structure screenshot:

![Python structure](https://github.com/MaxiAgrippa/ADTFinalProject/blob/master/screenshots/ProjectStructure.png)

# Step: Build application environment (web server, general configuration, etc.)

The Github repository is available at https://github.com/MaxiAgrippa/ADTFinalProject. At the moment, the application isn’t deployed to any web server or cloud environment, so it’s only running from the local environment.

# Step: Finance APIs

After testing a few possibilities in terms of APIs for collecting stock/financial data, including for example Alpha Vantage, Morning Star and many implementations of the Yahoo Finance API, the group decided to use one of the latter, which can be visualized at https://rapidapi.com/apidojo/api/yahoo-finance1. 

The connections between the API and the application, as well as between the application and MongoDB have been established and are working as expected.

Yahoo Finance API page:

![Yahoo Finance](https://github.com/MaxiAgrippa/ADTFinalProject/blob/master/screenshots/YahooFinanceAPI.png)

# Step: News APIs

PIP requirements:
pip install GoogleNews

Struggle and change in API:

1. first we decided to go with the "yahoo api" to get all information about stock news and quotes, but it doesn't return the date parameter which we want to use to query information for specific date. We tried to send date as a query string but that didn't succeed.
 
2. NewsAPi:- News api looks for a substring and return all data that matches the substring. so, most of the time it is not stock relevant data. That's why we choose to go with the GoogleNewsAPi.

We are using GoogleNewsAPi in this project to get all real time stock related news and quotes and for now it's working fine.

![Google News API](https://github.com/MaxiAgrippa/ADTFinalProject/blob/master/screenshots/GoogleNewsAPI.png)

# Other application requirements and comments (miscellaneous)

pip requirement:

pip install --upgrade requests

pip install -U pandas

pip install -U yfinance

pip install -U lxml

pip install -U pymongo

pip install -U dnspython

useful link:

Time convert between epoch second and normal:

https://www.epochconverter.com

Json beautify

https://jsonformatter.curiousconcept.com

Add document to an array

https://docs.mongodb.com/manual/reference/operator/update/addToSet/#up._S_addToSet

MongoDB aggregation pipeline

https://docs.mongodb.com/manual/core/aggregation-pipeline/

convert seconds since epoch to a `datetime` object

https://stackoverflow.com/questions/3694487/in-python-how-do-you-convert-seconds-since-epoch-to-a-datetime-object

Current Struggle:

1. choose yahoo financial API(YFA) or yfinancial?(Update!: alpha_vantage(maybe))
YFA have more information about schema, but the timestamp they are using need to convert. Moreover, it has limit.
yfinancial is totally free and don't have any access limit. BUT, the data schema is not obvious.
Temporary using YFA.

2. About data structure:(FIXED)
I guess we should give each company a "table", but currently we are only using one "table" for one company, I decide to go for it and fix it later.

3. Reduce the data duplication caused by add stock price data.
potential solution: https://stackoverflow.com/questions/14184099/fastest-way-to-remove-duplicate-documents-in-mongodb
Using aggregation to solve it.(FAIL)
ERROR: Data Structure Error Find, Need to adjust our data structure(schema)
Maybe we can set date to an unique index to solve it. When we insert new price data, we can set the insert command to skip those are duplicated in data?
