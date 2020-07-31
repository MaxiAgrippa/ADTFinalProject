from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd

key = "31e70ce77cmsh598f7175f032062p123b1fjsn8af3f9eff72a"
ts = TimeSeries(key=key, rapidapi=True, output_format='pandas', indexing_type='date')
pd.set_option('display.expand_frame_repr', False)

# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_daily_adjusted(symbol='AAPL', outputsize='compact')
print(data.to_json(orient="records", indent=2))
pprint(data.head(20))

# Because of this bug: https://github.com/matplotlib/matplotlib/pull/17983 (it will be fixed in the next release: 3.3.1)
plt.rcParams['date.epoch'] = '0000-12-31T00:00'

data['5. adjusted close'].plot()
plt.title('Daily Times Series for the AAPL stock (20 days)')
plt.show()
