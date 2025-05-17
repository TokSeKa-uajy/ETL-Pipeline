import time
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from transform import transform_data, transform_to_DataFrame
from datetime import datetime

from load import save_to_csv, store_to_postgre


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def fetching_content(url):
    """Mengambil konten HTML dari URL yang diberikan."""
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None

def extract_book_data(article):
    """Mengambil data buku berupa judul, harga, ketersediaan, dan rating dari article (element html)."""
    
    # Judul Barang
    book_title = article.find('h3').text.strip()
    book_title = book_title if book_title != 'Unknown Product' else 'N/A'
    
    # Ambil harga
    product_element = article.find('div', class_='price-container')
    price = product_element.find('span', class_='price').text.strip().replace('$', '') if product_element else 'N/A' #somehow replace gabisa di transform.py
    
    # Inisialisasi nilai default
    rating = colors = size = gender = 'N/A'
    
    # Ambil semua elemen <p> dalam price-container
    if article:
        for p in article.find_all('p'):
            text = p.get_text(strip=True)
            if text.startswith('Rating:'):
                match = re.search(r'(\d+(\.\d+)?)', text)
                rating = float(match.group(1)) if match else 'N/A'
            elif 'Colors' in text:
                match = re.search(r'\d+', text)
                colors = int(match.group()) if match else 'N/A'
            elif text.startswith('Size:'):
                size = text.replace('Size:', '').strip()
            elif text.startswith('Gender:'):
                gender = text.replace('Gender:', '').strip()
    
    timestamp = datetime.now()
    
    # Bangun dictionary hasil
    books = {
        "Title": book_title,
        "Price": price,
        "Rating": rating,
        "Colors": colors,
        "Size": size,
        "Gender": gender,
        "Timestamp": timestamp
    }

    return books

def scrape_book(base_url, start_page=1, delay=2):
    """Fungsi utama untuk mengambil keseluruhan data, mulai dari requests hingga menyimpannya dalam variabel data."""
    data = []
    page_number = start_page

    while True:
        if(page_number == 1):
            url = base_url
        elif(page_number <= 50):
            # Format URL untuk halaman berikutnya
            url = base_url + f"page{page_number}"
        else:
            print("Melewati halaman lebih dari 50")
            break
        
        try:
            print(f"Scraping halaman: {url}")
            content = fetching_content(url)
            if content:
                soup = BeautifulSoup(content, "html.parser")
                articles_element = soup.find_all('div', class_='product-details')
                for article in articles_element:
                    book = extract_book_data(article)
                    if 'N/A' not in book.values():
                        data.append(book)
    
                next_button = soup.find('li', class_='next')
                if next_button:
                    page_number += 1
                    time.sleep(delay) # Delay sebelum halaman berikutnya
                else:
                    break # Berhenti jika sudah tidak ada next button
            else:
                break # Berhenti jika ada kesalahan
        except Exception as e:
            print(f"❌ Error saat proses scraping halaman {url}: {e}")
            break  # keluar dari loop saat error besar
    return data


def main():
    """Fungsi utama untuk keseluruhan proses scraping hingga menyimpannya."""
    BASE_URL = 'https://fashion-studio.dicoding.dev/'
    all_books_data = scrape_book(BASE_URL)
    df = pd.DataFrame(all_books_data)
    print(df)
    if all_books_data:
        DataFrame = transform_to_DataFrame(all_books_data)   # Mengubah variabel all_books_data menjadi DataFrame.
        DataFrame = transform_data(DataFrame, 16000)   # Mentransformasikan data
        
        db_url = 'postgresql+psycopg2://developer:secretpassword@localhost:5432/produkdb'
        store_to_postgre(DataFrame, db_url) 
        
        print(DataFrame)
        save_to_csv(DataFrame)  # Menyimpan DataFrame ke dalam file CSV
    else:
        print("Tidak ada data yang ditemukan.")
    

if __name__ == '__main__':
    main()