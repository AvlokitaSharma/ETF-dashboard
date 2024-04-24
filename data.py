import pandas as pd
import numpy as np

# Generate a date range
dates = pd.date_range(start="2023-01-01", periods=365)  # One year of data

# Simulate ETF price movements
np.random.seed(0)  # for reproducibility
opens = 100 + np.cumsum(np.random.normal(0, 1, 365))  # Random walk model
highs = opens + np.random.uniform(1, 2, 365)  # Highs are always above opens
lows = opens - np.random.uniform(1, 2, 365)  # Lows are always below opens
closes = opens + np.random.normal(0, 1, 365)  # Close prices around open prices
adj_closes = closes * np.random.uniform(0.99, 1.01, 365)  # Adjusted closes slightly vary
volumes = np.random.randint(500000, 1000000, 365)  # Random volume data

# Create a DataFrame
etf_data = pd.DataFrame({
    'Date': dates,
    'Open': opens,
    'High': highs,
    'Low': lows,
    'Close': closes,
    'Adjusted Close': adj_closes,
    'Volume': volumes
})

# Print the first 10 rows to see the sample output
print(etf_data.head(10))
