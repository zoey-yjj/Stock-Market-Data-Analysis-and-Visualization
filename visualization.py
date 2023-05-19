# %%
import matplotlib.pyplot as plt
from market_data import fetch_stock_data
from data_analysis import analyze_stock_data

# Function for data visualization
def visualize_stock_data(stock_data):
    """
    Visualizes the stock market data.

    Args:
        stock_data (list): List of dictionaries containing stock market data

    Returns:
        None
    """
    df = analyze_stock_data(stock_data)

    plt.plot(df['date'], df['close'], label='Close')
    plt.plot(df['date'], df['moving_average'], label='Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Analysis')
    plt.legend()
    plt.show()

    # Plot the cumulative return and volatility
    plt.plot(df['date'], df['cumulative_return'], label='Cumulative Return')
    plt.plot(df['date'], df['volatility'], label='Volatility')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Cumulative Return and Volatility')
    plt.legend()
    plt.show()

    # Plot the RSI
    plt.plot(df['date'], df['rsi'])
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.title('Relative Strength Index (RSI)')
    plt.show()

'''
# Example usage
stock_symbol = 'AAPL'
stock_data = fetch_stock_data(stock_symbol)

if stock_data is not None:
    visualize_stock_data(stock_data)
'''

# %%
