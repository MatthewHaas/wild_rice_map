# 21 February 2020
# WD: /home/jkimball/haasx092/collection_map
# Skeleton code for plotting a map of Minnesota counties using geopandas
# Data come from MN GIS resource (https://gisdata.mn.gov/group/boundaries?q=&sort=title_string+asc)

# These should be run on the command line at the start of each session
export PYTHONPATH=/home/jkimball/haasx092/.conda/
export PYTHONPATH=/home/jkimball/haasx092/.conda/pkgs/descartes-1.1.0-py_4/site-packages/descartes
export PYTHONPATH=/home/jkimball/haasx092/lib/python/

import pandas as pd
import geopandas as gpd
import descartes
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point

#counties = "shp_bdry_counties/County_Boundaries_in_Minnesota.shp"
# I like the boundaries from the MN GIS source (projection is better), but the POLYGON geography coordinates do not work well with actual GPS coordinates (collection site data)
states = "cb_2018_us_county_20m/cb_2018_us_county_20m.shp" # ALL US counties (from: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)
collection_sites = "191106_wild_rice_samples.csv"

#map_counties = gpd.read_file(counties)
map_states = gpd.read_file(states) # read in counties
nwr_sites = pd.read_csv(collection_sites) # read in collection sites

# Select Minnesota from the US shape file
MN = map_states[map_states.STATEFP == '27'] #MN is 27. I should probably also add WI which is 55

# This section is for converting the latitude and longitude data into a form recognizable to geopandas
def make_point(row):
    return Point(row.Long, row.Lat) # Point() requires shapely.geometry

points = nwr_sites.apply(make_point, axis=1)
nwr_points = gpd.GeoDataFrame(nwr_sites, geometry=points)

# These lines of code are probably outdates/no longer needed, but I am keeping for now --commented out-- just in case I need to recover them
#map_counties.plot()
#variable = "COUNTY_NAM"

fig, ax = plt.subplots(1, figsize=(10,6))
MN.plot(color="white", linewidth=1.0, ax=ax, edgecolor="black")
nwr_points.plot(markersize=10, ax=ax, color="blue") # Need to figure out how to have each point be a unique color that I define to match R color scheme

ax.axis("off") # turn off the axis

fig.savefig("map_export.png", dpi=300)