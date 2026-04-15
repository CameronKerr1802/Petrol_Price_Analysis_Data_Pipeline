from datetime import datetime
import pandas as pd

def get_fuel_data():
    month = datetime.today().strftime('%m')
    year = datetime.now().year


    df = pd.read_csv(f"https://warsydprdstafuelwatch.blob.core.windows.net/historical-reports/FuelWatchRetail-{month}-{year}.csv")


    df["PUBLISH_DATE"] = pd.to_datetime(df["PUBLISH_DATE"], format="%d/%m/%Y")
    df["POSTCODE"] = df["POSTCODE"].astype(str)

    df.columns = map(lambda x: str(x).lower(), df.columns)

    print(df.info())
    print(df.head())
    print(df.isnull().sum())

    return df
