# Generated by Django 5.1.3 on 2024-11-11 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_yfinance', '0002_stockdata_delete_stock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('symbol', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=255, null=True)),
                ('long_name', models.CharField(max_length=255, null=True)),
                ('sector', models.CharField(max_length=255, null=True)),
                ('industry', models.CharField(max_length=255, null=True)),
                ('market_cap', models.BigIntegerField(null=True)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('exchange', models.CharField(max_length=50, null=True)),
                ('quote_type', models.CharField(max_length=50, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('open', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.BigIntegerField()),
                ('dividends', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('stock_splits', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fetch_yfinance.stockinfo')),
            ],
        ),
        migrations.DeleteModel(
            name='StockData',
        ),
        migrations.AddIndex(
            model_name='stockprice',
            index=models.Index(fields=['symbol', 'date'], name='fetch_yfina_symbol__daa518_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='stockprice',
            unique_together={('symbol', 'date')},
        ),
    ]
