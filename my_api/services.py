from datetime import datetime, timedelta
from django.db.models import Q
from fetch_yfinance.models import StockInfo, StockPrice
from django.db.models import Avg, Max, Min

class StockDataService:
    @staticmethod
    def get_stock_list():
        """Get list of all available stocks"""
        return StockInfo.objects.all()

    @staticmethod
    def get_stock_details(symbol):
        """Get detailed information for a specific stock"""
        return StockInfo.objects.filter(symbol=symbol).first()

    @staticmethod
    def get_stock_price_history(symbol, start_date=None, end_date=None):
        """Get price history for a stock within date range"""
        query = StockPrice.objects.filter(symbol=symbol)
        
        if start_date:
            query = query.filter(date__gte=start_date)
        if end_date:
            query = query.filter(date__lte=end_date)
            
        return query.order_by('date')

    @staticmethod
    def get_stock_summary(symbol, days=30):
        """Get summary statistics for a stock"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        prices = StockPrice.objects.filter(
            symbol=symbol,
            date__range=(start_date, end_date)
        )
        
        summary = prices.aggregate(
            avg_price=Avg('close'),
            max_price=Max('high'),
            min_price=Min('low'),
            avg_volume=Avg('volume')
        )
        
        return summary

    @staticmethod
    def search_stocks(query):
        """Search stocks by symbol or name"""
        return StockInfo.objects.filter(
            Q(symbol__icontains=query) |
            Q(short_name__icontains=query) |
            Q(long_name__icontains=query)
        ) 