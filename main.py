import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

from utils.extract import scrape_book
from utils.load import append_to_google_sheet, save_to_csv, store_to_postgre
from utils.transform import transform_data, transform_to_DataFrame


def main():
    """Fungsi utama untuk keseluruhan proses scraping hingga menyimpannya."""
    BASE_URL = 'https://fashion-studio.dicoding.dev/'
    all_books_data = scrape_book(BASE_URL)
    df = pd.DataFrame(all_books_data)
    print(df)
    if all_books_data:
        DataFrame = transform_to_DataFrame(all_books_data)   # Mengubah variabel all_books_data menjadi DataFrame.
        DataFrame = transform_data(DataFrame, 16000)   # Mentransformasikan data
        
        db_url = 'postgresql+psycopg2://developer:Seka%401904@localhost:5432/produkdb'
        store_to_postgre(DataFrame, db_url) 
        
        print(DataFrame)
        save_to_csv(DataFrame)  # Menyimpan DataFrame ke dalam file CSV
        DataFrame['Timestamp'] = pd.to_datetime(DataFrame['Timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
        append_to_google_sheet(DataFrame.values.tolist())  # Menyimpan DataFrame ke Google Sheets
    else:
        print("Tidak ada data yang ditemukan.")
    

if __name__ == '__main__':
    main()