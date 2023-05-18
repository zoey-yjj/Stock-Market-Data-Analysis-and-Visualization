from market_data import fetch_stock_data
from data_analysis import analyze_stock_data

# Function for portfolio management
def portfolio_management(stock_symbols):
    """
    Performs portfolio management by analyzing stock market data for multiple stocks.

    Args:
        stock_symbols (list): List of stock symbols

    Returns:
        None
    """
    portfolio_data = {}

    # Fetching and analyzing stock data for each stock symbol
    for symbol in stock_symbols:
        stock_data = fetch_stock_data(symbol)
        if stock_data is not None:
            analysis_result = analyze_stock_data(stock_data)
            portfolio_data[symbol] = analysis_result

    # Printing the portfolio data
    for symbol, analysis in portfolio_data.items():
        print(f"Stock Symbol: {symbol}")
        print(f"Average Close Price: {analysis['average_close_price']}")
        print(f"Minimum Close Price: {analysis['min_close_price']}")
        print(f"Maximum Close Price: {analysis['max_close_price']}")
        print(f"Average Volume: {analysis['total_volume']}")
        print()

# Example usage
stock_symbols = ['AAPL', 'GOOGL', 'TSLA']
portfolio_management(stock_symbols)
