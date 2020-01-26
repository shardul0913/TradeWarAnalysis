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


style.use('ggplot')

##Single company stock

class scrape:

    def singleStock(self,start,end,company,*args):

        fig = plt.figure()
        #the first arg is row*col second one is starting point for the graphs
        fig = plt.figure()
        df = web.DataReader(company, 'yahoo', start, end)
        df['100ma'] = df['Adj Close'].rolling(window=100).mean()
        df.dropna(inplace=True)
        df.to_csv(company + '.csv')
        df_ohlc = df['Adj Close'].resample('10D').ohlc()

        df_ohlc.reset_index(inplace=True)
        print(df)
        return df


    def web(self,industry):
        req = requests.get('https://www.forbes.com/global2000/list/#tab:overall')

        bsoup = bs.BeautifulSoup(req.text, features="lxml")
        print(bsoup)
        table = bsoup.find('table')
        company = []
        # print(table)
        for row in table.findAll('td'):
            print(row)
            company = row.findAll('td',{"class":"name"})
            print(company)

        return table
        #store the companies in the separate database


if __name__ == "__main__":

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2019, 10, 31)
    company = 'TSLA'
    links = scrape()
    linksReturn = links.singleStock(start,end,company)
    print(linksReturn)
