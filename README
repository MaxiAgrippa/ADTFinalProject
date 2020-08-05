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
# ERROR: Data Structure Error Find, Need to adjust our data structure(schema)
Maybe we can set date to an unique index to solve it. When we insert new price data, we can set the insert command to skip those are duplicated in data?

# Google News API

PIP requirements:
pip install GoogleNews

Struggle and change in API:
1. first we decided to go with the "yahoo api" to get all information about stock news and quotes, but it doesn't return the date parameter which we want to use to query information for 
 specific date. We tried to send date as a query string but that didn't succeed.
 
2. NewsAPi:- News api looks for a substring and return all data that matches the substring. so, most of the time it is not stock relevant data. That's why we choose to go with
the GoogleNewsAPi.

We are using GoogleNewsAPi in this project to get all real time stock related news and quotes and for now it's working fine.
