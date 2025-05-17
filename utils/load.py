import pandas as pd
from sqlalchemy import create_engine

# Menyimpan DataFrame ke dalam file CSV
def save_to_csv(data):
    """Menyimpan DataFrame ke dalam file CSV."""
    data.to_csv('products.csv', index=False)  

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