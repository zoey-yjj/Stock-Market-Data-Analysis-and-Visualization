# **Stock Data Analysis Project**

This project is designed to analyze stock market data and provide insights into the performance of different stocks. It includes functionality for data retrieval, analysis, visualization, and portfolio management.

## **Installation**

Clone the repository:

```
git clone https://github.com/zoey-yjj/Stock-Market-Data-Analysis-and-Visualization.git
```

Navigate to the project directory:

```
cd Stock-Market-Data-Analysis-and-Visualization
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## **Data Retrieval**

The data retrieval module fetches stock market data from an external API. To retrieve the data, use the retrieve_stock_data function and provide the necessary parameters such as the stock symbol, start date, and end date.


The retrieved stock data will be in the form of a list of data points, where each data point contains information such as the date, open price, close price, volume, etc.

## **Data Analysis**

The data analysis module provides functions to analyze the stock market data. The analyze_stock_data function calculates various metrics such as the average close price, minimum close price, maximum close price, and average volume.

The analysis_result dictionary will contain the calculated metrics based on the provided stock data.

## **Visualization**

The visualization module offers tools to visualize the stock market data and analysis results. The plot_stock_data function can be used to create line plots showing the trends in stock prices over time.

This will generate a line plot showing the stock prices over time.

## **Portfolio Management**

The portfolio management module helps manage a stock portfolio. It includes functions for calculating the portfolio value, returns, and allocation based on the provided stock data and portfolio holdings.

To calculate the portfolio value, use the calculate_portfolio_value function. Provide the stock data, portfolio holdings (stocks and quantities), and the date for which the portfolio value is to be calculated.

The portfolio_value variable will contain the calculated value of the portfolio on the specified date.

## **Testing and Error Handling**

The project includes comprehensive unit tests to ensure the correctness of the implemented functions. To run the tests, use the following command:

```
python -m unittest discover tests
```

The tests cover various scenarios and edge cases to validate the functionality and handle potential errors gracefully.
