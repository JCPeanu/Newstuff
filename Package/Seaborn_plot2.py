import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

pd.set_option('display.width', 110)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 30)
taxis = sns.load_dataset('taxis')

sns.barplot(data = taxis, x = 'passengers', y = 'tolls')
plt.show()
plt.close()

sns.displot(data = taxis,  x = 'total', col = 'color', row = 'payment')
plt.show()
plt.close()

sns.histplot(data = taxis, x = 'pickup_borough', hue = 'dropoff_borough', multiple = 'stack')
plt.show()
plt.close()

sns.scatterplot(data = taxis, x = 'fare', y = 'tip')
plt.show()
plt.close()

sns.kdeplot(data = taxis, x = 'distance', y = 'fare')
plt.show()
plt.close()