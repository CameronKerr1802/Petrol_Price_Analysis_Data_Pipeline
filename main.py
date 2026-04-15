
from db.connection import get_connection
from scripts.oil_price_scrape import get_oil_price
from scripts.fuel_price_scrape import get_fuel_data
from sql.query import OIL_BACKUP_QUERY, OIL_DELETE_MAIN_TABLE, OIL_INSERT_FROM_STAGING, add_hash_column_main, INSERT_INTO, FUEL_BACKUP_QUERY, TRUNCATE_STAGING_TABLE, add_hash_values_main
from sqlalchemy import text

#oil dataframe
oil_dataframe = get_oil_price(ticker = 'CL=F')
fuel_dataframe = get_fuel_data()


#Open connection to SQL Server
engine = get_connection()


with engine.begin() as conn:

    # 1. Load Dataframe to staging table
    oil_dataframe.to_sql('staging_table', con=engine, if_exists='replace', index=False)
    fuel_dataframe.to_sql('fuel_staging_table', con=conn, if_exists='append', index=False)

    # 2. Back up current tables for version control
    conn.execute(text(OIL_BACKUP_QUERY))
    conn.execute(text(FUEL_BACKUP_QUERY))

    # Clear Fuel Staging Table
    conn.execute(text(TRUNCATE_STAGING_TABLE))

    #3. Update table from oil staging table
    conn.execute(text(OIL_DELETE_MAIN_TABLE))
    conn.execute(text(OIL_INSERT_FROM_STAGING))

    #4. add hash column to fuelwatch table
    conn.execute(text(add_hash_column_main))

    #5 add hash values to fuelwatch table
    conn.execute(text(add_hash_values_main))
    
    #6 insert fuel staging table into fuelwatch table
    conn.execute(text(INSERT_INTO))

    conn.commit()

#Close Connection
    conn.close()