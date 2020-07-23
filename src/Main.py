from pprint import pprint
import yfinance as yf
msft = yf.Ticker("msft")
# pprint(msft.info)
# pprint(msft.recommendations)
pprint(msft.history(period="max"))

# data = yf.download("SPY AAPL", start="2019-04-01", end="2019-04-30")
# print(data)


def main():
    print("Main???\n")


if __name__ == '__main__':
    main()
