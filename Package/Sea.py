import matplotlib.pyplot as plt
import seaborn as sns
 
# seaborn has some example datasets
# print(sns.get_dataset_names())
 
# Load the data
# tips = sns.load_dataset("tips")
# print(tips)
# Create violinplot
# sns.violinplot(x = "total_bill", data=tips)
# Show the plot
# plt.show()
# plt.close()
#
# #relational plot
# sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker", style="smoker", size="size",)
# plt.show()
# plt.close()
#
# # Load iris data
iris = sns.load_dataset("iris")
# Construct iris plot
# sns.swarmplot(x="species", y="petal_length", data=iris)
# # Show plot
# plt.show()
# plt.close()
#
# # Load data
titanic = sns.load_dataset("titanic")
# Set up a factorplot
# g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", palette="muted", legend=False)
# # Show plot
# plt.show()
# plt.close()
#
# # Set up a factorplot
# g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", size=6, aspect=2, palette="muted", legend=False)
# #set logarithmic scale in the y axis
# g.set(yscale="log")
# # Show plot
# plt.show()
# plt.close()
#
import numpy as np
from matplotlib.colors import ListedColormap
#
# Define a variable N
N = 500
# Construct the colormap
current_palette = sns.color_palette("muted", n_colors=5)
cmap = ListedColormap(sns.color_palette(current_palette).as_hex())
# Initialize the data
data1 = np.random.randn(N)
data2 = np.random.randn(N)
# Assume that there are 5 possible labels
colors = np.random.randint(0,5,N)
# Create a scatter plot
plt.scatter(data1, data2, c=colors, cmap=cmap)
# Add a color bar
plt.colorbar()
# Show the plot
plt.show()
plt.close()
#
# penguins = sns.load_dataset("penguins")
# sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
# plt.show()
# plt.close()
#
# #subcharts within a violin plot
# sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
# plt.show()
# plt.close()
#
# #subcharts within a strip plot
# sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='smoker', dodge=True)
# plt.show()
# plt.close()
#
# #kde stands for kernel density
# sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
# plt.show()
# plt.close()
#
# #distribution plot
# sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="species")
# plt.show()
# plt.close()
#
# #joint plot
# sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")
# plt.show()
# plt.close()
#
# #histogram style for the joint plot
# sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", kind="hist")
# plt.show()
# plt.close()
#
# #this plot combines joint and marginal views, for maximum detail
# sns.pairplot(data=penguins, hue="species")
# plt.show()
# plt.close()
#
# # Set context to `"paper"`, change font size of the axes
# sns.set_context("paper", font_scale=2, rc={"font.size":8,"axes.labelsize":7})
# # Load iris data
# iris = sns.load_dataset("iris")
# # Construct iris plot
# sns.swarmplot(x="species", y="petal_length", data=iris)
# plt.title("Flowers")
# # Show plot
# plt.show()
# plt.close()
 