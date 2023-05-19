import unittest
import sys
sys.path.append('..')
from market_data import fetch_stock_data
from data_analysis import analyze_stock_data

# Function for portfolio management
def portfolio_management(stock_symbols):
    """
    Performs portfolio management by analyzing stock market data for multiple stocks.

    Args:
        stock_symbols (list): List of stock symbols

    Returns:
        dict: Dictionary containing portfolio data
    """
    portfolio_data = {}

    # Fetching and analyzing stock data for each stock symbol
    for symbol in stock_symbols:
        stock_data = fetch_stock_data(symbol)
        if stock_data is not None:
            analysis_result = analyze_stock_data(stock_data)
            portfolio_data[symbol] = analysis_result

    return portfolio_data

# Test case class for portfolio management
class PortfolioManagementTestCase(unittest.TestCase):
    def test_portfolio_management(self):
        stock_symbols = ["AAPL", "GOOGL", "MSFT"]
        portfolio_data = portfolio_management(stock_symbols)

        self.assertEqual(len(portfolio_data), len(stock_symbols))
        self.assertIsInstance(portfolio_data, dict)
        for symbol, analysis in portfolio_data.items():
            self.assertIn("average_close_price", analysis)
            self.assertIn("min_close_price", analysis)
            self.assertIn("max_close_price", analysis)
            self.assertIn("average_volume", analysis)

# Error handling example
def handle_error():
    try:
        stock_symbols = ["AAPL", "GOOGL", "MSFT"]
        portfolio_data = portfolio_management(stock_symbols)
        # Process portfolio data...
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Handle the error appropriately

# # Run the unit tests
# unittest.main()

# # Handle errors
# handle_error()
