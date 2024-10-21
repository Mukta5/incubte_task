import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine


def transform_data(df):
    df['Open_Date'] = pd.to_datetime(df['Open_Date'], format='%Y%m%d')
    df['Last_Consulted_Date'] = pd.to_datetime(df['Last_Consulted_Date'], format='%Y%m%d')
    df['DOB'] = pd.to_datetime(df['DOB'], format='%d%m%Y')

    # Derived columns: age and days since last consulted
    df['age'] = df['DOB'].apply(lambda x: datetime.now().year - x.year)
    df['days_since_last_consulted'] = (datetime.now() - df['Last_Consulted_Date']).dt.days
    return df


def load_data(df, table_name, db_engine):
    df.to_sql(table_name, con=db_engine, if_exists='replace', index=False)


if __name__ == "__main__":
    # Load sample data
    df = pd.read_csv('../data/customer_data.csv')

    # Transform the data
    df_transformed = transform_data(df)

    # Connect to MySQL
    engine = create_engine('mysql+mysqlconnector://root:Admin@localhost/hospital_db')

    # Load into staging table
    load_data(df_transformed, 'staging_customers', engine)

    # Filter for country-specific data and load
    df_india = df_transformed[df_transformed['Country'] == 'IND']
    load_data(df_india, 'india_customers', engine)
