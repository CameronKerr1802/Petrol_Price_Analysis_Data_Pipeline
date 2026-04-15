from dateutil.utils import today
import yfinance as yf
import pandas as pd

def get_oil_price(ticker):

    start_date = '2018-02-01'
    end_date = today()

    data = yf.download(ticker, start=start_date, end=end_date, multi_level_index=False)

    dataframe = pd.DataFrame(data)
    dataframe.reset_index(inplace=True)
    dataframe.drop(columns=['Volume'], inplace=True)
    print(dataframe)

    return dataframe

print(get_oil_price(ticker = 'CL=F'))