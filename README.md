# ETL Pipeline Project

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline using Python to process data from a fashion e-commerce website. The pipeline extracts product data through web scraping, transforms it into a structured format, and loads it into multiple destinations including PostgreSQL database, CSV files, and Google Sheets.

## Features
- Web scraping using BeautifulSoup4
- Data transformation using Pandas
- Multiple data storage options:
  - PostgreSQL database
  - CSV file export
  - Google Sheets integration
- Automated ETL process
- Unit testing implementation

## Technologies Used
- Python 3.x
- pandas: Data manipulation and analysis
- BeautifulSoup4: Web scraping
- psycopg2: PostgreSQL database connection
- Google Sheets API: Data storage in Google Sheets
- pytest: Unit testing

## Project Structure
```
ETL-Pipeline/
├── main.py                 # Main execution file
├── products.csv           # Output CSV file
├── requirements.txt       # Project dependencies
├── google-sheets-api.json # Google Sheets API credentials
├── utils/                 # Core functionality modules
│   ├── __init__.py
│   ├── extract.py        # Data extraction module
│   ├── transform.py      # Data transformation module
│   └── load.py           # Data loading module
└── test/                 # Test files
    ├── test_extract.py
    ├── test_transform.py
    └── test_load.py
```

## Setup and Installation
1. Clone the repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Configure PostgreSQL database connection
4. Set up Google Sheets API credentials
5. Run the application:
   ```
   python main.py
   ```

## Testing
Run the tests using pytest:
```
pytest
```

## Data Flow
1. **Extract**: Scrapes product data from the fashion e-commerce website
2. **Transform**: 
   - Converts raw data into DataFrame
   - Cleans and structures the data
   - Adds timestamps
3. **Load**:
   - Stores data in PostgreSQL database
   - Exports to CSV file
   - Uploads to Google Sheets

## Documentation
### Module Functions

#### extract.py
- `scrape_book(url)`: Scrapes product data from the given URL

#### transform.py
- `transform_to_DataFrame(data)`: Converts raw data to pandas DataFrame
- `transform_data(df, price_threshold)`: Processes and cleans the data

#### load.py
- `store_to_postgre(df, db_url)`: Stores DataFrame in PostgreSQL
- `save_to_csv(df)`: Exports DataFrame to CSV file
- `append_to_google_sheet(data)`: Uploads data to Google Sheets

## Author
Tok Se Ka