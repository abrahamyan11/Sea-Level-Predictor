import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

print(df.head())




plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='Line of Best Fit (All Data)')

recent_data = df[df['Year'] >= 2000]

slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

plt.plot(recent_data['Year'], slope_recent * recent_data['Year'] + intercept_recent, color='green', label='Line of Best Fit (2000 onwards)')

plt.plot([1880, 2050], [slope * 1880 + intercept, slope * 2050 + intercept], linestyle='--', color='red', label='Prediction to 2050 (All Data)')
plt.plot([2000, 2050], [slope_recent * 2000 + intercept_recent, slope_recent * 2050 + intercept_recent], linestyle='--', color='green', label='Prediction to 2050 (2000 onwards)')

plt.legend()

plt.savefig('sea_level_rise.png')
plt.show()
