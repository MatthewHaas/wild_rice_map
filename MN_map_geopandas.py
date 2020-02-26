# 25 February 2020
# WD: /home/jkimball/haasx092/collection_map
# Code for plotting a map of Minnesota & Wisconsin counties using geopandas
# Data come from US Census Bureau: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html

# Start an interactive python session (change wall time based on need)
#qsub -I -l nodes=1:ppn=4,mem=8gb,walltime=0:20:00 -q interactive

# Load python3
module load python3

# These should be run on the command line at the start of each session
export PYTHONPATH=/home/jkimball/haasx092/.conda/
export PYTHONPATH=/home/jkimball/haasx092/.conda/pkgs/descartes-1.1.0-py_4/site-packages/descartes
export PYTHONPATH=/home/jkimball/haasx092/lib/python/

# Launch python
ipython

import pandas as pd
import geopandas as gpd
import descartes
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point # for Point()
import shapely.geometry
from matplotlib.lines import Line2D
import Cartopy as ccrs # for scale bar


# The issue of projection data from the US Census has been fixed; it's OK to use this file now.
states = "cb_2018_us_county_20m/cb_2018_us_county_20m.shp" # ALL US counties
collection_sites = "200224_wild_rice_samples.csv" # This updated file has GPS coordinates converted to Universal Transverse Mercator (UTM) format

map_states = gpd.read_file(states) # read in counties
nwr_sites = pd.read_csv(collection_sites) # read in collection sites

# This code is crucial to achieving the projection that I want (matches the great MN GIS data)
map_states = map_states.to_crs({"init" : "epsg:26915"})

# Select Minnesota from the US shape file
#These lines of code are not needed if I stick with the shape file provided by the State of Minnesota versus the Census Bureau
MN_WI = map_states[(map_states.STATEFP == "27") | (map_states.STATEFP == "55")] # MN is 27 and WI is 55


# This section is for converting the latitude and longitude data into a form recognizable to geopandas
# The issue with the original projection issue is that the latitude and longitude needed to be converted to UTM format. I did the conversion of GPS coordinates with an online tool and created new columns in the CSV file containing the sample collection data.
def make_point(row):
    return Point(row.UTM_easting, row.UTM_northing) # Point() requires shapely.geometry

points = nwr_sites.apply(make_point, axis=1)
nwr_points = gpd.GeoDataFrame(nwr_sites, geometry=points)

# Not a very elegant approach, but this is how I think I need to go about plotting unique colors for each lake
aquatica = nwr_points[nwr_points.Location == "Aquatica_species"]
bass = nwr_points[nwr_points.Location == "Bass Lake"]
bigfork = nwr_points[nwr_points.Location == "Big Fork River"]
clearwater = nwr_points[nwr_points.Location == "Clearwater River"]
dahler = nwr_points[nwr_points.Location == "Dahler Lake"]
decker = nwr_points[nwr_points.Location == "Decker Lake"]
garfield = nwr_points[nwr_points.Location == "Garfield Lake"]
mudhen = nwr_points[nwr_points.Location == "Mud Hen Lake"]
necktie = nwr_points[nwr_points.Location == "Necktie River"]
ottertail = nwr_points[nwr_points.Location == "Ottertail River"]
phantom = nwr_points[nwr_points.Location == "Phantom Lake"]
plantagenet = nwr_points[nwr_points.Location == "Plantagenet"]
shell = nwr_points[nwr_points.Location == "Shell Lake"]
upperrice= nwr_points[nwr_points.Location == "Upper Rice Lake"]

# Start the plotting
fig, ax = plt.subplots(1, figsize=(20,15))
MN_WI.plot(color="white", linewidth=1.0, ax=ax, edgecolor="black")
aquatica.plot(marker="^", markersize=75, ax=ax, color="#cd0000" ) # Aquatica
bass.plot(markersize=75, ax=ax, color="#ff0000") # Bass Lake
#bigfork.plot(markersize=75, ax=ax, color="#cd8500")# Big Fork River
clearwater.plot(markersize=75, ax=ax, color="#ffa600") # Clearwater River
dahler.plot(markersize=75, ax=ax, color="#cdcd00") # Dahler Lake
decker.plot(markersize=75, ax=ax, color="#ffff00") # Decker Lake
garfield.plot(markersize=75, ax=ax, color="#00cd00") # Garfield Lake
mudhen.plot(markersize=75, ax=ax, color="#00ff00") # Mud Hen Lake
necktie.plot(markersize=75, ax=ax, color="#00008b") # Necktie River
ottertail.plot(markersize=75, ax=ax, color="#0000ff") # Ottertail River
phantom.plot(markersize=75, ax=ax, color="#cd3278") # Phantom Lake
plantagenet.plot(markersize=75, ax=ax, color="#ee82ee") # Plantagenet
shell.plot(markersize=75, ax=ax, color="#541a8b") # Shell Lake
upperrice.plot(markersize=75, ax=ax, color="#a020f0") # Upper Rice Lake

# Generate info for legend
legend_points = [Line2D([0],[0], color="#cd0000", marker="^", linestyle="none", label="$\it{Z. aquatica}$"), 
				 Line2D([0],[0], color="#ff0000", marker="o", linestyle="none", label="Bass Lake"), 
				 #Line2D([0],[0], color="#cd8500", marker="o", linestyle="none", label="Big Fork River"), 
				 Line2D([0],[0], color="#ffa600", marker="o", linestyle="none", label="Clearwater River"), 
				 Line2D([0],[0], color="#cdcd00", marker="o", linestyle="none", label="Dahler Lake",), 
				 Line2D([0],[0], color="#ffff00", marker="o", linestyle="none", label="Decker Lake"), 
				 Line2D([0],[0], color="#00cd00", marker="o", linestyle="none", label="Garfield Lake"), 
				 Line2D([0],[0], color="#00ff00", marker="o", linestyle="none", label="Mud Hen Lake"), 
				 Line2D([0],[0], color="#00008b", marker="o", linestyle="none", label="Necktie River"), 
				 Line2D([0],[0], color="#0000ff", marker="o", linestyle="none", label="Ottertail River"), 
				 Line2D([0],[0], color="#cd3278", marker="o", linestyle="none", label="Phantom Lake"), 
				 Line2D([0],[0], color="#ee82ee", marker="o", linestyle="none", label="Plantagenet"), 
				 Line2D([0],[0], color="#541a8b", marker="o", linestyle="none", label="Shell Lake"), 
				 Line2D([0],[0], color="#a020f0", marker="o", linestyle="none", label="Upper Rice Lake")]

# Plot the legend
ax.legend(handles=legend_points, loc="lower right", facecolor="white") # I thought facecolor would make background white vs. partially transparent. Maybe I'm using it wrong?


fig.suptitle("Northern Wild Rice Collection Sites", family="serif")
ax.axis("off") # turn off the axis

fig.savefig("map_export.png", dpi=300)