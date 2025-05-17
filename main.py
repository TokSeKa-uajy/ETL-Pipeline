# from utils.extract import scrape_book
# from utils.load import save_to_csv, store_to_postgre
# from utils.transform import transform_data, transform_to_DataFrame

# def main():
#     """Fungsi utama untuk keseluruhan proses scraping hingga menyimpannya."""
#     BASE_URL = 'https://fashion-studio.dicoding.dev/'
#     all_books_data = scrape_book(BASE_URL)
#     df = pd.DataFrame(all_books_data)
#     print(df)
#     if all_books_data:
#         DataFrame = transform_to_DataFrame(all_books_data)   # Mengubah variabel all_books_data menjadi DataFrame.
#         DataFrame = transform_data(DataFrame, 16000)   # Mentransformasikan data
        
#         db_url = 'postgresql+psycopg2://developer:secretpassword@localhost:5432/produkdb'
#         store_to_postgre(DataFrame, db_url) 
        
#         print(DataFrame)
#         save_to_csv(DataFrame)  # Menyimpan DataFrame ke dalam file CSV
#     else:
#         print("Tidak ada data yang ditemukan.")

# if __name__ == '__main__':
#     main()