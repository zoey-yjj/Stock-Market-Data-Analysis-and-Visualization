from market_data import fetch_stock_data
from data_analysis import analyze_stock_data


# Function for portfolio management
def portfolio_management(stock_symbols, investment_amount):
    # Get the stock data for each symbol
    stock_data = []
    for symbol in stock_symbols:
        data = fetch_stock_data(symbol)
        stock_data.append(data)

    # Perform analysis for each stock
    stock_ranks = {}
    for i, data in enumerate(stock_data):
        analysis_result = analyze_stock_data(data)
        stock_ranks[stock_symbols[i]] = analysis_result['daily_return'].mean()

    # Rank the stocks based on daily return
    ranked_stocks = sorted(stock_ranks.items(), key=lambda x: x[1], reverse=True)

    # Calculate investment amount for each stock based on rank
    total_ranks = sum([rank for _, rank in ranked_stocks])
    stock_investments = {}
    for symbol, rank in ranked_stocks:
        allocation_percentage = (rank / total_ranks) * 100
        investment = (allocation_percentage / 100) * investment_amount
        stock_investments[symbol] = investment

    return stock_investments

'''
# Example usage
stock_symbols = ['AAPL', 'GOOGL', 'MSFT']  # Example stock symbols
investment_amount = 1000
portfolio = portfolio_management(stock_symbols, investment_amount)
print(portfolio)
'''
