from utils.extract import extract_book_data, fetching_content, scrape_book

from unittest import TestCase
from unittest.mock import patch
from bs4 import BeautifulSoup
from datetime import datetime

class TestExtract(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_fetching_content_returns_not_none(self):
        url = 'https://fashion-studio.dicoding.dev/'
        result = fetching_content(url)
        assert result is not None
        
    def test_extract_book_data_missing_fields(self):
        html = """
        <div class="product-details">
            <h3>Unknown Product</h3>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find('div', class_='product-details')

        result = extract_book_data(article)

        assert result["Title"] == "N/A"
        assert result["Price"] == "N/A"
        
    def test_scrape_book_not_empty(self):
        result = scrape_book("https://fashion-studio.dicoding.dev/")
        assert isinstance(result, list)
        assert len(result) > 0

