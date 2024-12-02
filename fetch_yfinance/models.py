from django.db import models

class StockInfo(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    long_name = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)
    market_cap = models.BigIntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    exchange = models.CharField(max_length=50, null=True, blank=True)
    quote_type = models.CharField(max_length=50, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol

class StockPrice(models.Model):
    symbol = models.ForeignKey(StockInfo, on_delete=models.CASCADE)
    date = models.DateTimeField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()
    dividends = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    stock_splits = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    value1 = models.FloatField(null=True, blank=True)
    value2 = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('symbol', 'date')
        indexes = [
            models.Index(fields=['symbol', 'date']),
        ]

    def __str__(self):
        return f"{self.symbol} - {self.date}"