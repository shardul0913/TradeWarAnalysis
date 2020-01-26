import quandl
import pandas as pd
import datetime as dt
import time
import datetime as dt
import yahoo_finance
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import datetime, quandl
import pandas as pd
import requests
import bs4 as bs
import datetime, quandl

# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2019, 8, 30)
#
# ndq = quandl.get("NASDAQOMX/COMP-NASDAQ",
#               trim_start=start,
#               trim_end=end,paginate=True)
#
# ndq = ndq.dropna()
#
# export_excel = ndq.to_excel(r'nasdaq.xlsx', index = None, header=True)

# print(ndq.head(4))

reque = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(reque.text, 'lxml')
pgtable = soup.find('table', {'class': 'wikitable sortable'})
ticks = []

start_default = dt.datetime(2015, 1, 1)
end_default = dt.datetime.now()

for row in pgtable.findAll('tr')[2:]:
    tick = row.findAll('td')[0].text
    ticks.append(tick)

df = web.DataReader('BRK', 'yahoo', start_default, end_default)

print(df)