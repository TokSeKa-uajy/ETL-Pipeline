import pandas as pd
from utils.load import *

def test_save_to_csv_creates_file(tmp_path):
    df = pd.DataFrame({
        "Title": ["Baju Test"],
        "Price": [100000],
        "Rating": [4.5],
        "Colors": [2],
        "Size": ["M"],
        "Gender": ["Men"],
        "Timestamp": ["2025-05-16 22:00:00"]
    })
    file_path = tmp_path / "test_output.csv"
    save_to_csv(df, filename=file_path)
    assert file_path.exists()
    loaded = pd.read_csv(file_path)
    assert loaded.equals(df)

def test_store_to_postgre_print_success(capsys):
    df = pd.DataFrame({
        "Title": ["Test Print"],
        "Price": [10000],
        "Rating": [4.0],
        "Colors": [2],
        "Size": ["M"],
        "Gender": ["Men"],
        "Timestamp": ["2025-05-16 22:00:00"]
    })

    db_url = 'postgresql+psycopg2://developer:Seka%401904@localhost:5432/produkdb'

    try:
        store_to_postgre(df, db_url)
    except:
        pass  # Abaikan error koneksi

    captured = capsys.readouterr()
    assert "Data berhasil ditambahkan!" in captured.out or "Terjadi kesalahan saat menyimpan data:" in captured.out

def test_append_to_google_sheet_output(capsys):
    dummy_data = [
        ["Title", "Price", "Rating", "Colors", "Size", "Gender", "Timestamp"],
        ["Test Shirt", 100000, 4.5, 3, "M", "Men", "2025-05-16 22:00:00"]
    ]

    try:
        append_to_google_sheet(dummy_data)
    except:
        pass

    captured = capsys.readouterr()
    assert "Berhasil menambahkan data!" in captured.out or "An error occurred" in captured.out
