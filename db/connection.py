import urllib.parse
from sqlalchemy import create_engine
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    print(pyodbc.drivers())
    params = urllib.parse.quote_plus(f"DRIVER={"{ODBC Driver 17 for SQL Server}"};SERVER={os.getenv("DB_SERVER")};DATABASE={os.getenv("DB")};Trusted_Connection=yes;Encrypt=yes;TrustServerCertificate=yes")
    conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    engine = create_engine(conn_str)
    #conn = engine.raw_connection()
    return engine
print(get_connection())
