from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fetch_yfinance.models import StockInfo, StockPrice
from datetime import datetime, timedelta

class StockAPITests(APITestCase):

    def setUp(self):
        # Create test data for StockInfo
        self.stock_info = StockInfo.objects.create(
            symbol='AMZN',
            short_name='Amazon.com Inc.',
            long_name='Amazon.com Inc.',
            sector='Consumer Discretionary',
            industry='Internet Retail',
            market_cap=1600000000000,
            currency='USD',
            exchange='NASDAQ',
            quote_type='EQUITY'
        )

        # Create test data for StockPrice
        self.stock_price = StockPrice.objects.create(
            date=datetime(2024, 11, 15, 9, 30),
            open=3200.00,
            high=3250.00,
            low=3150.00,
            close=3225.00,
            volume=100000,
            symbol_id='AMZN'
        )

        self.stock_price2 = StockPrice.objects.create(
            date=datetime(2024, 11, 30, 9, 30),
            open=3225.00,
            high=3300.00,
            low=3200.00,
            close=3280.00,
            volume=150000,
            symbol_id='AMZN'
        )

    def test_stock_list(self):
        """Test the stock_list endpoint"""
        url = reverse('stock_list')  # Ensure this matches your URL configuration
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # We created one stock
        self.assertEqual(response.data[0]['symbol'], 'AMZN')
        self.assertEqual(response.data[0]['short_name'], 'Amazon.com Inc.')

    def test_price_data(self):
        """Test the price-data endpoint for a specific symbol and date range"""
        url = reverse('price-data') + '?symbol=AMZN&start_date=2024-11-25&end_date=2024-11-30'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['symbol'], 'AMZN')
        self.assertEqual(response.data[0]['open'], 3200.00)
        self.assertEqual(response.data[1]['close'], 3280.00)
