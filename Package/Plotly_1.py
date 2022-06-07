import plotly.graph_objects as go
import plotly.express as px
 
print(px.data.__all__)
 
iris = px.data.iris()
#
# #scatter plot
# fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
# fig.show()
#
# #trend lines
# fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
#                  marginal_y="violin", marginal_x="box", trendline="ols",
#                  template="simple_white")
# fig.show()
#
# #error bars
# iris["e"] = iris["sepal_width"]/100
# fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
#                  error_x="e", error_y="e")
# fig.show()
#
# #bar charts
tips = px.data.tips()
# fig = px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group")
# fig.show()
#
medals = px.data.medals_long()
 
# fig = px.bar(medals, x="medal", y="count", color="nation",
#              pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"])
# fig.show()
#
# #facet plots
# fig = px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group",
#              facet_row="time", facet_col="day",
#        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
# fig.show()
#
# #scatterplot matrices
# fig = px.scatter_matrix(iris, dimensions=["sepal_width", "sepal_length",
#                                           "petal_width", "petal_length"], color="species")
# fig.show()
#
# #parellel categories
# fig = px.parallel_coordinates(iris, color="species_id", labels={"species_id": "Species",
#                   "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
#                   "petal_width": "Petal Width", "petal_length": "Petal Length", },
#     color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
# fig.show()
#
# fig = px.parallel_categories(tips, color="size", color_continuous_scale=px.colors.sequential.Inferno)
# fig.show()
#
# #hover labels
gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop",
#                  color="continent", hover_name="country", log_x=True, size_max=60)
# fig.show()
#
# #animations
# fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year",
#                  animation_group="country", size="pop", color="continent",
#                  hover_name="country", facet_col="continent", log_x=True,
#                  size_max=45, range_x=[100,100000], range_y=[25,90])
# fig.show()
#
# #line charts
# fig = px.line(gapminder, x="year", y="lifeExp", color="continent",
#               line_group="country", hover_name="country",
#               line_shape="spline", render_mode="svg")
# fig.show()
#
# #area charts
# fig = px.area(gapminder, x="year", y="pop", color="continent", line_group="country")
# fig.show()
#
# #timeline charts
import pandas as pd
#
# df = pd.DataFrame([
#     dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
#     dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
#     dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
# ])

# fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
# fig.show()
#
# #funnel charts
# data = dict(
#     number=[39, 27.4, 20.6, 11, 2],
#     stage=["Website visit", "Downloads", "Potential customers",
#            "Requested price", "Invoice sent"])
# fig = px.funnel(data, x='number', y='stage')
# fig.show()
#
# #pie charts
# df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
# df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
# fig = px.pie(df, values='pop', names='country', title='Population of European continent')
# fig.show()
#
# #sunburst charts
# df = px.data.gapminder().query("year == 2007")
# fig = px.sunburst(df, path=['continent', 'country'], values='pop',
#                   color='lifeExp', hover_data=['iso_alpha'])
# fig.show()
#
# #tree maps
# fig = px.treemap(gapminder, path=[px.Constant('world'), 'continent', 'country'], values='pop',
#                   color='lifeExp', hover_data=['iso_alpha'])
# fig.show()
#
# #icicle charts
# fig = px.icicle(gapminder, path=[px.Constant('world'), 'continent', 'country'], values='pop',
#                   color='lifeExp', hover_data=['iso_alpha'])
# fig.show()
#
# #histograms
fig = px.histogram(tips, x="total_bill", y="tip", color="sex", marginal="rug",
                   hover_data=tips.columns)
fig.show()

#boxplots
fig = px.box(tips, x="day", y="total_bill", color="smoker", notched=True)
fig.show()

# #violin plots
# fig = px.violin(tips, y="tip", x="smoker", color="sex", box=True,
#                 points="all", hover_data=df.columns)
# fig.show()
#
# #cummulative distribution charts
# fig = px.ecdf(tips, x="total_bill", color="sex")
# fig.show()
#
# #strip charts
# fig = px.strip(tips, x="total_bill", y="time", orientation="h", color="smoker")
# fig.show()
#
# #density contour charts
# fig = px.density_contour(iris, x="sepal_width", y="sepal_length")
# fig.show()
#
# #density heatmaps
# fig = px.density_heatmap(iris, x="sepal_width", y="sepal_length", marginal_x="rug", marginal_y="histogram")
# fig.show()
#
# data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
# fig = px.imshow(data,
#                 labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
#                 x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
#                 y=['Morning', 'Afternoon', 'Evening']
#                )
# fig.update_xaxes(side="top")
# fig.show()
#
# #tile maps
carshare = px.data.carshare()
# fig = px.scatter_mapbox(carshare, lat="centroid_lat", lon="centroid_lon",
#                 color="peak_hour", size="car_hours",
#                 color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
#                 mapbox_style="carto-positron")
# fig.show()
#
election = px.data.election()
# geojson = px.data.election_geojson()
# fig = px.choropleth_mapbox(election, geojson=geojson, color="Bergeron",
#                            locations="district", featureidkey="properties.district",
#                            center={"lat": 45.5517, "lon": -73.7073},
#                            mapbox_style="carto-positron", zoom=9)
# fig.show()
#
# #outline maps
# fig = px.scatter_geo(gapminder, locations="iso_alpha", color="continent",
#                 hover_name="country", size="pop",
#                 animation_frame="year", projection="natural earth")
# fig.show()
#
# #polar plots
wind = px.data.wind()
# fig = px.scatter_polar(wind, r="frequency", theta="direction", color="strength",
#         symbol="strength", color_discrete_sequence=px.colors.sequential.Plasma_r)
# fig.show()
#
# #radar charts
# fig = px.line_polar(wind, r="frequency", theta="direction", color="strength",
#         line_close=True, color_discrete_sequence=px.colors.sequential.Plasma_r)
# fig.show()
#
# #polar bar charts
# fig = px.bar_polar(wind, r="frequency", theta="direction", color="strength",
#         template="plotly_dark", color_discrete_sequence= px.colors.sequential.Plasma_r)
# fig.show()
#
# #3D scatter plots
# fig = px.scatter_3d(election, x="Joly", y="Coderre", z="Bergeron", color="winner",
#         size="total", hover_name="district", symbol="result",
#         color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"})
# fig.show()
#
# #ternay charts
# fig = px.scatter_ternary(election, a="Joly", b="Coderre", c="Bergeron", color="winner",
#         size="total", hover_name="district", size_max=15,
#         color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"} )
# fig.show()