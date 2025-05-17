import pandas as pd
import re

def transform_to_DataFrame(data):
    """Mengubah data menjadi DataFrame."""
    df = pd.DataFrame(data)
    return df

def transform_data(data, exchange_rate):
    """Menggabungkan semua transformasi data menjadi satu fungsi dengan error handling."""

    try:
        print("Transformasi Price ke float")
        temp = data['Price'].astype(float)
    except Exception as e:
        print("Gagal mengubah kolom Price ke float:", e)
        raise

    try:
        print("Mengalikan Price dengan exchange rate")
        data['Price'] = (temp * exchange_rate).astype(float)
    except Exception as e:
        print("Gagal menghitung harga dalam Rupiah:", e)
        raise

    try:
        print("Transformasi tipe data kolom lainnya")
        data['Title'] = data['Title'].astype('string')
        data['Size'] = data['Size'].astype('string')
        data['Gender'] = data['Gender'].astype('string')
        data['Colors'] = data['Colors'].astype(int)
    except Exception as e:
        print("Gagal mengubah tipe data:", e)
        raise

    return data
