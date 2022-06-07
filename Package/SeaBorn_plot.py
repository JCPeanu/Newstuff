import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

pd.set_option('display.width', 110)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 30)
car_crashes = sns.load_dataset('car_crashes')
# print(car_crashes)
# print(car_crashes.columns)

# sns.pointplot(data = car_crashes, x = "abbrev", y = "total")
# plt.show()
# plt.close()

# sns.lmplot(data = car_crashes, x = "speeding", y = "alcohol")
# plt.show()
# plt.close()

diamonds = sns.load_dataset('diamonds')
print(diamonds)
print(diamonds.columns)

# sns.scatterplot(data = diamonds, x = "carat", y = "price", hue = "cut")
# plt.show()
# plt.close()

# sns.violinplot(data = diamonds, x = "clarity", y = "depth")
# plt.show()
# plt.close()

# sns.scatterplot(data = diamonds, x = "table", y = "color")
# plt.show()
# plt.close()

mpg = sns.load_dataset('mpg')
print(mpg)
# sns.pairplot(data = mpg, x_vars = ["displacement", "horsepower", "weight", "acceleration"], y_vars = ["displacement", "horsepower", "weight", "acceleration"])
# plt.show()
# plt.close()

planets = sns.load_dataset('planets')
print(planets)
print(planets.columns)
# sns.jointplot(data = planets, x = "orbital_period", y = "mass")
# plt.show()
# plt.close()

sns.pairplot(data = planets, x_vars = ["orbital_period", "mass", "distance", "method"], y_vars = ["orbital_period", "mass", "distance", "method"])
plt.show()
plt.close()