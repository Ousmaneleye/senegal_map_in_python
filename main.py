import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("senegal-with-regions_.geojson")

# renames the values of the column "name" ("Dakar Region" => "Dakar")
gdf.name = gdf.name.apply(lambda x: x.split()[0])


fig, ax = plt.subplots(figsize=(18, 10))
gdf.plot(ax=ax, column="name", legend=True, cmap="tab20b")
ax.set_axis_off()

plt.show()