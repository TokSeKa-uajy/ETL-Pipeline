import pandas as pd
from utils.transform import transform_data

def test_transform_data_success():
    # DataFrame dummy
    df = pd.DataFrame({
        'Title': ['Kaos'],
        'Price': [10000],
        'Rating': [4.5],  # tidak diproses dalam fungsi ini, boleh ada
        'Colors': [3],
        'Size': ['M'],
        'Gender': ['Unisex']
    })

    exchange_rate = 1.6
    result = transform_data(df.copy(), exchange_rate)

    # Verifikasi hasil
    assert isinstance(result['Price'][0], float)
    assert result['Price'][0] == 16000.0
    assert result['Title'].dtype.name == 'string'
    assert result['Colors'].dtype == 'int32' or result['Colors'].dtype == 'int64'
