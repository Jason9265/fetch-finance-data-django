from django.db import models

class StockPrice(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically incrementing ID
    date = models.DateTimeField()  # Date and time of the stock price
    open = models.FloatField()  # Opening price
    high = models.FloatField()  # Highest price
    low = models.FloatField()  # Lowest price
    close = models.FloatField()  # Closing price
    volume = models.BigIntegerField()  # Volume of stocks traded
    dividends = models.FloatField(null=True, blank=True)  # Dividends, if any
    stock_splits = models.FloatField(null=True, blank=True)  # Stock splits, if any
    symbol_id = models.CharField(max_length=10)  # Stock symbol ID
    value1 = models.FloatField(null=True, blank=True)  # Additional value 1
    value2 = models.FloatField(null=True, blank=True)  # Additional value 2

    def __str__(self):
        return f"{self.symbol_id} - {self.date}"
