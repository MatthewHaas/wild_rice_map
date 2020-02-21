# 21 February 2020
# WD: /home/jkimball/haasx092/collection_map
# Skeleton code for plotting a map of Minnesota counties using geopandas
# Data come from MN GIS resource (https://gisdata.mn.gov/group/boundaries?q=&sort=title_string+asc)

import pandas as pd
import geopandas as gpd
import descartes
import matplotlib.pyplot as plt
import numpy as np

counties = "shp_bdry_counties/County_Boundaries_in_Minnesota.shp"

map_counties = gpd.read_file(counties)

map_counties.plot()

variable = "COUNTY_NAM"

fig, ax = plt.subplots(1, figsize=(10,6))
map_counties.plot(column=variable, cmap="Blues", linewidth=0.8, ax=ax, edgecolor='0.8')

fig.savefig("map_export.png", dpi=300)