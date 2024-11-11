from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from .services import StockDataService
from .serializers import StockInfoSerializer, StockPriceSerializer

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
