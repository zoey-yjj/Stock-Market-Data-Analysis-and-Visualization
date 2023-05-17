import requests
import json

# Alpha Vantage API endpoint and your API key
API_ENDPOINT = 'https://www.alphavantage.co/query'
API_KEY = 'K4AWQU4G77G6EMZP'

def fetch_stock_data(symbol):
    """
    Fetches stock market data for a given symbol using the Alpha Vantage API.

    Args:
        symbol (str): Stock symbol (e.g., 'AAPL' for Apple Inc.)

    Returns:
        dict: Stock market data as a dictionary
    """
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': API_KEY
    }

    try:
        response = requests.get(API_ENDPOINT, params=params)
        data = response.json()

        # Check if the API request was successful
        if 'Error Message' in data:
            print('Error:', data['Error Message'])
            return None

        # Extract the daily stock data
        time_series = data['Time Series (Daily)']

        # Process the stock data
        stock_data = []
        for date, values in time_series.items():
            stock_data.append({
                'date': date,
                'open': float(values['1. open']),
                'high': float(values['2. high']),
                'low': float(values['3. low']),
                'close': float(values['4. close']),
                'volume': int(values['6. volume'])
            })

        return stock_data

    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

# Example usage
stock_symbol = 'AAPL'
stock_data = fetch_stock_data(stock_symbol)

if stock_data is not None:
    print(f"Stock Data for {stock_symbol}:")
    for data in stock_data:
        print(f"Date: {data['date']}, Close: {data['close']}, Volume: {data['volume']}")
