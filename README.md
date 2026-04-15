# ⛽ Petrol Price Analysis Data Pipeline ⛽

### Overview

This project is a data pipeline and analysis workbook that focuses on Western Australian fuel prices
as well as Yahoo Finance Crude Oil prices.
It collects, cleans, transforms and uploads the data to a Microsoft SQL Database. It is used
to analyse fuel price data to uncover trends, correlations, and insights into how fuel prices vary over 
time and region.

This project demonstrates a complete end to end data analytic pipeline, with data ingestion, preprocessing,
and SQL integration.
#
### Tech Stack

- Python (Pandas, yfinance, SQLAlchemy, pyodbc)
- SQL Server
- Power BI
- Hashing techniques for duplicate detection
#
### Key Features
- Automated data ingestion from FuelWatch and Yahoo Finance
- Data cleaning and standardisation pipeline
- Hash-based duplicate detection for data integrity
- SQL Server integration for persistent storage
- Exploratory data analysis and visualisation in Power BI
#
### PIPELINE WORKFLOW

1. Data ingestion:
   
   Fuel prices are loaded into dataframes from a URL using pandas .read_csv() function
   
2. Data Cleaning:

   - Standardised column formats
   - Converted data types for analysis
   
3. Data validation:

   Since the dataset is refreshed every three days, the CSV file that is retrieved from the
   FuelWatch website contains both new and previously published records. As a result,
   re-uploading the file to the database introduces the risk of duplicate entries.
   To address this, a hash-based approach was implemented for duplicate detection.
   By generating a unique hash for each row based on its key attributes, the pipeline
   can efficiently identify and prevent duplicate records from being inserted into the
   database.
  
4. Cleaned data is stored in SQL Server tables for querying and reporting
   
5. Analysis & Insights:
   
   Exploratory data analysis is performed to identify:
   - Price trends over time
   - Regional Price differences
   - Correlation between unleaded and oil prices
   - YoY price changes
#
### Power BI Dashboard

https://app.powerbi.com/links/F8gVVrRGop?ctid=c00d4c1b-cf7b-4e93-b7c7-10113a9bc230&pbi_source=linkShare

Includes
- Interacitve fuel price trends
- Regional comparisons
- Time based filtering
- Location based filtering

#
### Future Imporvements

- Automate the process using Airflow
- Implement a time series forecasting model for fuel price prediciton.

#
### Author

Cameron Kerr

Data Analytics / Data Engineering Project

GitHub: CameronKerr1802

![Python](https://img.shields.io/badge/Python-3.10-blue)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-red)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
