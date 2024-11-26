import yfinance as yf
from decimal import Decimal
from .models import StockInfo, StockPrice

def update_stock_info(symbol):
    """
    Fetch and update stock information
    """
    ticker = yf.Ticker(symbol)
    info = ticker.info
    
    stock_info, created = StockInfo.objects.update_or_create(
        symbol=symbol,
        defaults={
            'short_name': info.get('shortName'),
            'long_name': info.get('longName'),
            'sector': info.get('sector'),
            'industry': info.get('industry'),
            'market_cap': info.get('marketCap'),
            'currency': info.get('currency'),
            'exchange': info.get('exchange'),
            'quote_type': info.get('quoteType'),
        }
    )
    return stock_info

def fetch_stock_data(symbol, period="1mo", interval="1d"):
    """
    Fetch stock price history and store in database
    """
    stock_info = update_stock_info(symbol)
    
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval, actions=True)
    
    for index, row in df.iterrows():
        StockPrice.objects.update_or_create(
            symbol=stock_info,
            date=index,
            defaults={
                'open': Decimal(str(row['Open'])),
                'high': Decimal(str(row['High'])),
                'low': Decimal(str(row['Low'])),
                'close': Decimal(str(row['Close'])),
                'volume': int(row['Volume']),
                'dividends': Decimal(str(row['Dividends'])),
                'stock_splits': Decimal(str(row['Stock Splits']))
            }
        )

def mass_download_stocks(symbols, period="1mo", interval="1d"):
    """
    Download data for multiple stocks at once
    """
    for symbol in symbols:
        update_stock_info(symbol)
    
    data = yf.download(
        " ".join(symbols),
        period=period,
        interval=interval,
        group_by="ticker",
        actions=True
    )
    
    for symbol in symbols:
        stock_info = StockInfo.objects.get(symbol=symbol)
        symbol_data = data[symbol]
        
        for index, row in symbol_data.iterrows():
            StockPrice.objects.update_or_create(
                symbol=stock_info,
                date=index,
                defaults={
                    'open': Decimal(str(row['Open'])),
                    'high': Decimal(str(row['High'])),
                    'low': Decimal(str(row['Low'])),
                    'close': Decimal(str(row['Close'])),
                    'volume': int(row['Volume']),
                    'dividends': Decimal(str(row.get('Dividends', 0))),
                    'stock_splits': Decimal(str(row.get('Stock Splits', 0)))
                }
            )