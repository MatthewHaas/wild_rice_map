# 21 February 2020
# WD: /home/jkimball/haasx092/collection_map
# Making map of Minnesota watersheds using geopandas
# I don't think the current shape file has all of the data we need (it seems to be only a partial list of watersheds)
# Still, the code should be considered a skeleton that could be replaced with more complete data

import pandas as pd
import geopandas as gpd
import descartes
import matplotlib.pyplot as plt
import numpy as np

watersheds = "watershed_management_districts_and_orgs/watershed_management_districts_and_organizations.shp"

map_watersheds = gpd.read_file(watersheds)

map_watersheds.plot()

variable = "TYPE"

fig, ax = plt.subplots(1, figsize=(10,6))
map_watersheds.plot(column=variable, cmap="Blues", linewidth=0.8, ax=ax, edgecolor='0.8')

fig.savefig("map_export.png", dpi=300)