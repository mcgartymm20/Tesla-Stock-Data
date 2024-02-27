import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

# Fetch historical data for Tesla stock
tesla = yf.download('TSLA', start='2019-01-01', end='2024-01-01')

# Calculate moving averages
tesla['MA50'] = tesla['Close'].rolling(window=50).mean()
tesla['MA200'] = tesla['Close'].rolling(window=200).mean()

# Plot candlestick chart with moving averages
mpf.plot(tesla, type='candle', mav=(50, 200), volume=True, title='Tesla Stock Analysis',
         ylabel='Price', ylabel_lower='Volume', style='yahoo', figratio=(16,8), tight_layout=True)

# Highlight crossover points
crossovers = []

for i in range(1, len(tesla)):
    if tesla['MA50'][i] > tesla['MA200'][i] and tesla['MA50'][i - 1] <= tesla['MA200'][i - 1]:
        crossovers.append((tesla.index[i], tesla['Close'][i], 'Golden Cross'))
    elif tesla['MA50'][i] < tesla['MA200'][i] and tesla['MA50'][i - 1] >= tesla['MA200'][i - 1]:
        crossovers.append((tesla.index[i], tesla['Close'][i], 'Death Cross'))

for date, price, label in crossovers:
    plt.text(date, price, label, fontsize=10, color='red', ha='center', va='center')

plt.show()
