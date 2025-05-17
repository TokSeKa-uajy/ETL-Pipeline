import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Menyimpan DataFrame ke dalam file CSV
def save_to_csv(data, filename='products.csv'):
    """Menyimpan DataFrame ke dalam file CSV."""
    data.to_csv(filename, index=False)

def store_to_postgre(data, db_url):
    """Fungsi untuk menyimpan data ke dalam PostgreSQL."""
    try:
        # Membuat engine database
        engine = create_engine(db_url)
        
        # Menyimpan data ke tabel 'produktoscrape' jika tabel sudah ada, data akan ditambahkan (append)
        with engine.connect() as con:
            data.to_sql('produktoscrape', con=con, if_exists='append', index=False)
            print("Data berhasil ditambahkan!")
    
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")
        

# Menyimpan DataFrame ke Google Sheets
def append_to_google_sheet(values): #Link : https://docs.google.com/spreadsheets/d/1B5ESSIp0st53PveOnvlF3FDduU-sbqXakFt_FAaZ_a0/
    SERVICE_ACCOUNT_FILE = './my-project-84579-460115-2d05df3c9e66.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1B5ESSIp0st53PveOnvlF3FDduU-sbqXakFt_FAaZ_a0'
    RANGE_NAME = 'Sheet1!A2:G1000'
    """
    Menambahkan data ke Google Sheets.
    :param values: List of lists, setiap sublist adalah satu baris data.
    """
    try:
        credential = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=credential)
        sheet = service.spreadsheets()
        body = {'values': values}
        result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption='RAW',
            body=body
        ).execute()
        print("Berhasil menambahkan data!")
    except Exception as e:
        print(f"An error occurred: {e}")

