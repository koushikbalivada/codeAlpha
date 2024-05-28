import yfinance as yf
import pandas as pd

# Define the stock symbols and the number of shares
portfolio = {
    'TSLA': 10,
    'AAPL': 15,
    'NFLX': 5,
    'GOOGL': 2
}

# Fetch stock data
data = yf.download(list(portfolio.keys()), period='1d', progress=False)

# Ensure the data was fetched successfully
if not data.empty:
    # Calculate current prices
    prices = data['Close'].iloc[-1]

    # Calculate the value of each stock holding
    portfolio_value = {stock: shares * prices[stock] for stock, shares in portfolio.items()}

    # Create a DataFrame for better visualization
    portfolio_df = pd.DataFrame(list(portfolio_value.items()), columns=['Stock', 'Value'])
    portfolio_df['Shares'] = portfolio_df['Stock'].map(portfolio)
    portfolio_df['Price'] = portfolio_df['Stock'].map(prices)

    # Calculate the total value of the portfolio
    total_value = portfolio_df['Value'].sum()

    # Display the portfolio
    print(portfolio_df)
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")
else:
    print("Failed to fetch data. Please check the stock symbols.")
