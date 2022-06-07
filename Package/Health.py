from matplotlib import markers
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import time
import random

raw = pd.read_csv("Health Indicators - Data.csv")
print(raw)

only_one_indicator = raw.loc[raw['Indicator Name'] == 'Labor force, total']
print(only_one_indicator)

modified_data = only_one_indicator.melt(id_vars=['Country Name'], value_vars = raw.columns[2:].values)
print(modified_data)

# fig = px.line(modified_data, x = "variable", y = "value", color = "Country Name", markers = True)
# fig.show()
# fig.close()

sns.lineplot(data = modified_data, x = 'variable', y = 'value', hue = "Country Name")
plt.xlabel("Year")
plt.show()
plt.close()