# Generated by Django 5.1.3 on 2024-11-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_yfinance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('open', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddIndex(
            model_name='stockdata',
            index=models.Index(fields=['symbol', 'date'], name='fetch_yfina_symbol_ca001e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='stockdata',
            unique_together={('symbol', 'date')},
        ),
    ]
