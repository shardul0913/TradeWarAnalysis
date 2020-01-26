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
from dataScrape import scrape1
import matplotlib.dates as mdates
import plotly.express as pe


style.use('seaborn-ticks')
style.use('dark_background')

#Single company stock

def plotSingle(scrapeObj,start,end,company):

    fig = plt.figure()
    fig.subplots_adjust(hspace=1.4)
    #the first arg is row*col second one is starting point for the graphs

    scraoeObj = scrapeObj
    df1 = scrapeObj.sp500_data(company,start,end)

    df1 = df1.set_index(pd.DatetimeIndex(df1['Date']))
    df1['100ma'] = df1['Adj Close'].rolling(window=100).mean()
    df1.dropna(inplace=True)
    df1.to_csv(company + '.csv')

    print(pd.Index(df1))

    df_ohlc = df1['Adj Close'].resample('10D').ohlc()
    df_volume = df1['Volume'].resample('10D').sum()

    df_ohlc.reset_index(inplace=True)
    df_ohlc['Date'] = pd.to_datetime(df_ohlc['Date']).dt.date
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    ax1.xaxis_date()

    candlestick_ohlc(ax1, df_ohlc.values, width=5, colorup='g')
    ax1.plot(df1.index, df1['Adj Close'],linewidth= 0.25)

    ax1.title.set_text(company + ' Stock Performance')
    ax1.set_xlabel('Stock Price')
    ax1.set_ylabel('Date Range')

    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0,facecolor='g')
    ax2.title.set_text(company + ' Stock Volume')
    ax2.set_xlabel('Stock Volume')
    ax2.set_ylabel('Date Range')
    plt.show()
    ndq = quandl.get("NASDAQOMX/COMP-NASDAQ",
                     trim_start='2018-03-01',
                     trim_end='2019-04-03')

def sp500_plot():

    df = pd.DataFrame(dict(
        r=[1, 5, 2, 2, 3],
        theta=['processing cost', 'mechanical properties', 'chemical stability',
               'thermal stability', 'device integration']))
    fig = pe.line_polar(df, r='r', theta='theta', line_close=True)
    fig.show()

    print('hi')


def main():

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2019, 8, 30)
    company = 'ACN'
    scrapeObj = scrape1()
    plotSingle(scrapeObj,start,end,company)
    sp500_plot()

main()