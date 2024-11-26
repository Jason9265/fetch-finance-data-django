# fetch-finance-data-django
Fetch historical stock prices


## How to run this project
1. clone repo
```git clone https://github.com/Jason9265/fetch-finance-data-django.git```

2. active virtual environment
Windows:
```finance-env\Scripts\activate```

macOS/Linux:
```source finance-env/bin/activate```

3. Install required packages
```pip install -r requirements.txt```

4. fetch stocks by stock name
```python manage.py fetch_stocks AAPL --period 1y --interval 1d```

Or fetch multiple stocks
```python manage.py fetch_stocks AAPL GOOGL MSFT --batch```