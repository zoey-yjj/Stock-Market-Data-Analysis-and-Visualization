# %%
import matplotlib.pyplot as plt
from market_data import fetch_stock_data

# Function for data visualization
def visualize_stock_data(stock_data):
    """
    Visualizes the stock market data.

    Args:
        stock_data (list): List of dictionaries containing stock market data

    Returns:
        None
    """
    dates = [data['date'] for data in stock_data]
    close_prices = [data['close'] for data in stock_data]
    volume = [data['volume'] for data in stock_data]

    # Plotting the closing prices
    plt.figure(figsize=(12, 6))
    plt.plot(dates, close_prices)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Stock Closing Prices')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    # Plotting the volume
    plt.figure(figsize=(12, 6))
    plt.plot(dates, volume, color='green')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('Stock Volume')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Example usage
stock_symbol = 'AAPL'
stock_data = fetch_stock_data(stock_symbol)

if stock_data is not None:
    visualize_stock_data(stock_data)
