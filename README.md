# Customer ETL Pipeline

## Project Description

This ETL pipeline processes customer data for a multi-specialty hospital chain and loads it into country-specific tables. The pipeline:

- Extracts customer data from a CSV file
- Transforms the data (calculates derived columns such as `age` and `days_since_last_consulted`)
- Loads the transformed data into staging and country-specific MySQL tables

## Project Structure

- `data/` - Contains sample customer data in CSV format
- `src/` - Contains the ETL pipeline code
- `sql/` - SQL scripts for creating tables and running data validations
- `requirements.txt` - Python dependencies




