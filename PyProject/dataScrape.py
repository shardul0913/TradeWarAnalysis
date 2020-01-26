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
import time

#database library
import os
import sqlite3
from sqlite3 import Error

style.use('seaborn-ticks')
##Single company stock

class scrape1:

    def singleStock(self,start,end,company,*args):
        #the first arg is row*col second one is starting point for the graphs
        #create database
        db_file = 'Stocks.db'
        connection = self.createDB(db_file, delete_db=True)
        c = connection.cursor()
        c.execute('SELECT COUNT(name) FROM sqlite_master WHERE type=\'table\' AND name=\'{'+company+'}\';')

        if c.fetchone()[0] == 0:
            df = web.DataReader(company, 'yahoo', start, end)
            df['100ma'] = df['Adj Close'].rolling(window=100).mean()
            df.dropna(inplace=True)
            df.to_sql(company, connection, if_exists='replace', index=True, index_label=None, chunksize=None,dtype=None, method=None)
            connection.commit()
            #close the connection
            print('1')
            return df

        else:
            print('2')
            cur = connection.cursor()
            cur.execute("SELECT * FROM "+company)
            rows = cur.fetchall()
            for row in rows:
                print(row)

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

    def createDB(self,db_file,delete_db=True):

        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
                print(e)

    def Quandl(self,connection,start,end):

        ndq = quandl.get("NASDAQOMX/COMP-NASDAQ",
                         trim_start='2018-03-01',
                         trim_end='2019-04-03')

        export_excel = ndq.to_excel(r'nasdaq.xlsx', index=None, header=True)
        print(ndq)
        # ndq.to_sql('Quandl', connection, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None,
        #           method=None)

    def sp500_data(self,company,start,end):

        start_default = dt.datetime(2000, 1, 1)
        end_default = dt.datetime(2019, 8, 3)
        reque = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        soup = bs.BeautifulSoup(reque.text, 'lxml')
        pgtable = soup.find('table', {'class': 'wikitable sortable'})
        ticks = []

        for row in pgtable.findAll('tr')[1:]:
            tick = row.findAll('td')[0].text
            ticks.append(tick.strip('\n'))

        print(ticks)

        if os.path.exists('sp500.db'):

            print('Already DB present')
            connec500 = sqlite3.connect('sp500.db')
            print("SELECT * FROM " + company + " WHERE Date BETWEEN '" +str(start_default )+ "' AND '" +str(end_default)+"'")

            df = pd.read_sql_query("SELECT * FROM " + company + " WHERE Date BETWEEN '" +str(start_default )+ "' AND '" +str(end_default)+"'", connec500)


            return df

        elif not os.path.exists('sp500.db'):
            try:
                connec500 = sqlite3.connect('sp500.db')
            except Error as e:
                print(e)
            for names in ticks:
                time.sleep(5)
                print(names)

                df = web.DataReader(names, 'yahoo', start_default, end_default)
                df['100ma'] = df['Adj Close'].rolling(window=100).mean()
                df.dropna(inplace=True)
                df.to_sql(names, connec500, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None,
                          method=None)
                connec500.commit()
            connec500 = sqlite3.connect('sp500.db')
            c = connec500.cursor()
            df = pd.read_sql_query("SELECT * FROM " + company, c)


            return df