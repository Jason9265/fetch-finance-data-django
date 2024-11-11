from rest_framework import serializers
from fetch_yfinance.models import StockInfo, StockPrice

class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = '__all__'

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = '__all__' 