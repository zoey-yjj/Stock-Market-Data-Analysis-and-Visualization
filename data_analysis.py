# %%
import numpy as np
import matplotlib.pyplot as plt
from market_data import fetch_stock_data

# Function for data analysis
def analyze_stock_data(stock_data):
    """
    Performs basic analysis on the stock market data.

    Args:
        stock_data (list): List of dictionaries containing stock market data

    Returns:
        dict: Dictionary with analysis results
    """
    close_prices = [data['close'] for data in stock_data]
    volume = [data['volume'] for data in stock_data]

    analysis_results = {
        'max_close_price': np.max(close_prices),
        'min_close_price': np.min(close_prices),
        'average_close_price': np.mean(close_prices),
        'total_volume': np.sum(volume)
    }

    return analysis_results

# Example usage
stock_symbol = 'AAPL'
stock_data = fetch_stock_data(stock_symbol)

if stock_data is not None:
    analysis_results = analyze_stock_data(stock_data)

    print(f"Stock Data Analysis for {stock_symbol}:")
    print(f"Max Close Price: {analysis_results['max_close_price']}")
    print(f"Min Close Price: {analysis_results['min_close_price']}")
    print(f"Average Close Price: {analysis_results['average_close_price']}")
    print(f"Total Volume: {analysis_results['total_volume']}")

    # Plotting the closing prices
    dates = [data['date'] for data in stock_data]
    close_prices = [data['close'] for data in stock_data]

    plt.plot(dates, close_prices)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title(f"{stock_symbol} Stock Closing Prices")
    plt.xticks(rotation=45)
    plt.show()
