# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from market_data import fetch_stock_data


# Function for data analysis
def analyze_stock_data(stock_data):
    # Convert stock_data to a pandas DataFrame
    df = pd.DataFrame(stock_data)

    # Calculate average volume
    df['average_volume'] = df['volume'].mean()

    # Calculate moving average
    df['moving_average'] = df['close'].rolling(window=5).mean()

    # Calculate daily returns
    df['daily_return'] = df['close'].pct_change()

    # Calculate cumulative returns
    df['cumulative_return'] = (1 + df['daily_return']).cumprod()

    # Calculate volatility
    df['volatility'] = df['daily_return'].rolling(window=20).std()

    # Calculate relative strength index (RSI)
    delta = df['close'].diff()
    gain = delta.mask(delta < 0, 0)
    loss = -delta.mask(delta > 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))

    # Perform benchmarking - calculate the time taken for specific operations
    start_time = pd.Timestamp.now()

    # Perform additional analysis or benchmarks here

    end_time = pd.Timestamp.now()
    elapsed_time = end_time - start_time

    # Print the elapsed time for benchmarking purposes
    print(f"Elapsed Time: {elapsed_time}")

    # Return the updated DataFrame with analysis results
    return df

'''
# Example usage
stock_symbol = 'AAPL'
stock_data = fetch_stock_data(stock_symbol)

if stock_data is not None:
    analysis_result = analyze_stock_data(stock_data)
    print(analysis_result)
'''
# %%
