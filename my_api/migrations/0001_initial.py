# Generated by Django 5.1.3 on 2024-12-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('dividends', models.FloatField(blank=True, null=True)),
                ('stock_splits', models.FloatField(blank=True, null=True)),
                ('symbol_id', models.CharField(max_length=10)),
                ('value1', models.FloatField(blank=True, null=True)),
                ('value2', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
