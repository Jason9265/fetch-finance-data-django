from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from .services import StockDataService
from .serializers import StockInfoSerializer, StockPriceSerializer
from datetime import datetime, timedelta

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StockInfoSerializer
    
    def get_queryset(self):
        return StockDataService.get_stock_list()
    
    @action(detail=True, methods=['get'])
    def price_history(self, request, pk=None):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if start_date:
            start_date = parse_date(start_date)
        if end_date:
            end_date = parse_date(end_date)
            
        prices = StockDataService.get_stock_price_history(pk, start_date, end_date)
        serializer = StockPriceSerializer(prices, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        days = int(request.query_params.get('days', 30))
        summary = StockDataService.get_stock_summary(pk, days)
        return Response(summary)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        stocks = StockDataService.search_stocks(query)
        serializer = self.get_serializer(stocks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='price-data')
    def price_data(self, request):
        symbol = request.query_params.get('symbol')
        period = int(request.query_params.get('period', 30))  # Default to 30 days

        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        # If start_date or end_date is not provided, calculate them based on the period
        if not start_date or not end_date:
            end_date = datetime.now().date()  # Get only the date part
            start_date = end_date - timedelta(days=period)  # Calculate start date

        # Ensure start_date and end_date are strings before parsing
        if isinstance(start_date, str) and isinstance(end_date, str):
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
        else:
            # If they are not strings, we can convert the calculated dates to strings
            start_date = start_date.strftime('%Y-%m-%d') if isinstance(start_date, datetime) else start_date
            end_date = end_date.strftime('%Y-%m-%d') if isinstance(end_date, datetime) else end_date

        # Get the price history for the specified symbol and date range
        prices = StockDataService.get_stock_price_history(symbol, start_date, end_date)

        # Format the response data with trend indicator
        formatted_prices = [
            [
                price.id,
                price.date,
                price.open,
                price.high,
                price.low,
                price.close,
                price.volume,
                price.symbol_id,
                1 if price.close > price.open else -1,  # Trend indicator
            ]
            for price in prices
        ]

        return Response(formatted_prices)

    @action(detail=False, methods=['get'], url_path='stock_list')
    def stock_list(self, request):
        stocks = StockDataService.get_stock_list()
        
        formatted_stocks = [
            [
                stock.symbol,
                stock.short_name,
                stock.long_name,
                stock.sector,
                stock.industry,
                stock.market_cap,
                stock.currency,
                stock.exchange,
                stock.quote_type,
                stock.last_updated,
            ]
            for stock in stocks
        ]
        return Response(formatted_stocks)

    @action(detail=False, methods=['get'], url_path='stock-detail')
    def fetch_stock_detail(self, request):
        symbol = request.query_params.get('symbol')
        
        if not symbol:
            return Response({"error": "Symbol parameter is required."}, status=400)

        stock_info = StockDataService.get_stock_details(symbol)

        if stock_info is None:
            return Response({"error": "Stock not found."}, status=404)

        stock_info=[
            stock_info.symbol,
            stock_info.short_name,
            stock_info.long_name,
            stock_info.sector,
            stock_info.industry,
            stock_info.market_cap,
            stock_info.currency,
            stock_info.exchange,
            stock_info.quote_type,
            stock_info.last_updated,
        ]
        print(stock_info)
        return Response(stock_info) 
