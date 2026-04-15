from datetime import datetime


timestamp = datetime.now().strftime('%Y%m%d')
OIL_BACKUP_QUERY = f"SELECT * INTO dbo.oil_price_backup_{timestamp} FROM dbo.oil_price"

OIL_DELETE_MAIN_TABLE = "DELETE FROM dbo.oil_price;"

OIL_INSERT_FROM_STAGING = "INSERT INTO dbo.oil_price SELECT * FROM dbo.staging_table;"

FUEL_BACKUP_QUERY = f"SELECT * INTO dbo.fuel_price_backup_{timestamp} FROM dbo.fuelwatch"



add_hash_column_main = """IF NOT EXISTS (
                              SELECT 1
                              FROM sys.columns
                              WHERE Name = 'row_hash'
                              AND Object_ID = Object_ID('dbo.fuelwatch')
                         )    
                          BEGIN
                                ALTER TABLE dbo.fuelwatch
                                ADD row_hash VARCHAR(64);
                          END;"""
add_hash_values_main = """UPDATE dbo.fuelwatch
                          SET row_hash = CONVERT(VARCHAR(64), HASHBYTES('SHA2_256',
                                CONCAT(
                                publish_date,
                                trading_name,
                                brand_description,
                                product_description,
                                product_price,
                                address,
                                location,
                                postcode,
                                area_description,
                                region_description)),2)
                          WHERE row_hash IS NULL;"""

INSERT_INTO = """
INSERT INTO dbo.fuelwatch (
    publish_date,
        trading_name,
        brand_description,
        product_description,
        product_price,
        address,
        location,
        postcode,
        area_description,
        region_description,
    row_hash
)
SELECT
    t.publish_date,
        t.trading_name,
        t.brand_description,
        t.product_description,
        t.product_price,
        t.address,
        t.location,
        t.postcode,
        t.area_description,
        t.region_description,
    t.row_hash
FROM fuel_staging_table t
LEFT JOIN dbo.fuelwatch s
    ON t.row_hash = s.row_hash
WHERE s.row_hash IS NULL;"""

TRUNCATE_STAGING_TABLE = """TRUNCATE TABLE dbo.fuel_staging_table"""