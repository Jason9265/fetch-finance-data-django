from django.db import models

class StockInfo(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)  # Set symbol as the primary key
    short_name = models.CharField(max_length=255, null=True, blank=True)
    long_name = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)
    market_cap = models.BigIntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    exchange = models.CharField(max_length=50, null=True, blank=True)
    quote_type = models.CharField(max_length=50, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)  # Automatically set to now when saved

    def __str__(self):
        return self.symbol
