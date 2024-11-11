from django.core.management.base import BaseCommand
from fetch_yfinance.services import fetch_stock_data, mass_download_stocks

class Command(BaseCommand):
    help = 'Fetch stock data from Yahoo Finance'

    def add_arguments(self, parser):
        parser.add_argument('symbols', nargs='+', type=str)
        parser.add_argument(
            '--period',
            type=str,
            default='1mo',
            help='Data period (1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd)'
        )
        parser.add_argument(
            '--interval',
            type=str,
            default='1d',
            help='Data interval (1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo)'
        )
        parser.add_argument(
            '--batch',
            action='store_true',
            help='Use batch download for multiple symbols'
        )

    def handle(self, *args, **options):
        symbols = options['symbols']
        period = options['period']
        interval = options['interval']
        
        if options['batch'] and len(symbols) > 1:
            self.stdout.write(f'Batch downloading data for {len(symbols)} symbols...')
            try:
                mass_download_stocks(symbols, period=period, interval=interval)
                self.stdout.write(self.style.SUCCESS('Successfully downloaded all data'))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download data: {str(e)}')
                )
        else:
            for symbol in symbols:
                try:
                    self.stdout.write(f'Fetching data for {symbol}...')
                    fetch_stock_data(symbol, period=period, interval=interval)
                    self.stdout.write(
                        self.style.SUCCESS(f'Successfully fetched data for {symbol}')
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Failed to fetch data for {symbol}: {str(e)}')
                    ) 