import mysql.connector
from mysql.connector import errorcode

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Admin',
            database='hospital_db'
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

# Create staging and country-specific tables
def create_tables(connection):
    cursor = connection.cursor()

    with open('../sql/create_staging_table.sql', 'r') as f:
        staging_table_query = f.read()
        cursor.execute(staging_table_query)

    with open('../sql/create_country_tables.sql', 'r') as f:
        country_tables_query = f.read()
        for query in country_tables_query.split(';'):
            if query.strip():
                cursor.execute(query)

    connection.commit()
    cursor.close()

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    conn.close()
