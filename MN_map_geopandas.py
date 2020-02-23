# 21 February 2020
# WD: /home/jkimball/haasx092/collection_map
# Skeleton code for plotting a map of Minnesota counties using geopandas
# Data come from MN GIS resource (https://gisdata.mn.gov/group/boundaries?q=&sort=title_string+asc)

# These should be run on the command line at the start of each session
export PYTHONPATH=/home/jkimball/haasx092/.conda/
export PYTHONPATH=/home/jkimball/haasx092/.conda/pkgs/descartes-1.1.0-py_4/site-packages/descartes
export PYTHONPATH=/home/jkimball/haasx092/lib/python/

# Start an interactive python session (change wall time based on need)
#qsub -I -l nodes=1:ppn=4,mem=8gb,walltime=0:20:00 -q interactive

module load python3
ipython

import pandas as pd
import geopandas as gpd
import descartes
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point # for Point()
from matplotlib.lines import Line2D 
import Cartopy.crs as ccrs # for scale bar

#counties = "shp_bdry_counties/County_Boundaries_in_Minnesota.shp"
# I like the boundaries from the MN GIS source (projection is better), but the POLYGON geography coordinates do not work well with actual GPS coordinates (collection site data)
states = "cb_2018_us_county_20m/cb_2018_us_county_20m.shp" # ALL US counties (from: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)
collection_sites = "191106_wild_rice_samples.csv"

#map_counties = gpd.read_file(counties)
map_states = gpd.read_file(states) # read in counties
nwr_sites = pd.read_csv(collection_sites) # read in collection sites

# Select Minnesota from the US shape file
MN = map_states[map_states.STATEFP == "27"] #MN is 27. I should probably also add WI which is 55
WI = map_states[map_states.STATEFP == "55"]

# This section is for converting the latitude and longitude data into a form recognizable to geopandas
def make_point(row):
    return Point(row.Long, row.Lat) # Point() requires shapely.geometry

points = nwr_sites.apply(make_point, axis=1)
nwr_points = gpd.GeoDataFrame(nwr_sites, geometry=points)

# These lines of code are probably outdates/no longer needed, but I am keeping for now --commented out-- just in case I need to recover them
#map_counties.plot()
#variable = "COUNTY_NAM"
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

fig, ax = plt.subplots(1, figsize=(12,8))
MN.plot(color="white", linewidth=1.0, ax=ax, edgecolor="black")
WI.plot(color="white", linewidth=1.0, ax=ax, edgecolor="black")
ax.set_xlim(-97.3,-89.6)
ax.set_ylim(43,50)
aquatica.plot(marker="^", markersize=20, ax=ax, color="#cd0000" ) # Aquatica
bass.plot(markersize=20, ax=ax, color="#ff0000") # Bass Lake
bigfork.plot(markersize=20, ax=ax, color="#cd8500")# Big Fork River
clearwater.plot(markersize=20, ax=ax, color="#ffa600") # Clearwater River
dahler.plot(markersize=20, ax=ax, color="#cdcd00") # Dahler Lake
decker.plot(markersize=20, ax=ax, color="#ffff00") # Decker Lake
garfield.plot(markersize=20, ax=ax, color="#00cd00") # Garfield Lake
mudhen.plot(markersize=20, ax=ax, color="#00ff00") # Mud Hen Lake
necktie.plot(markersize=20, ax=ax, color="#00008b") # Necktie River
ottertail.plot(markersize=20, ax=ax, color="#0000ff") # Ottertail River
phantom.plot(markersize=20, ax=ax, color="#cd3278") # Phantom Lake
plantagenet.plot(markersize=20, ax=ax, color="#ee82ee") # Plantagenet
shell.plot(markersize=20, ax=ax, color="#541a8b") # Shell Lake
upperrice.plot(markersize=20, ax=ax, color="#a020f0") # Upper Rice Lake

# Generate info for legend
legend_points = [Line2D([0],[0], color="#cd0000", marker="^", label="\textit{Z. aquatica}"), 
				 Line2D([0],[0], color="#ff0000", marker="o", label="Bass Lake"), 
				 Line2D([0],[0], color="#cd8500", marker="o", label="Big Fork River"), 
				 Line2D([0],[0], color="#ffa600", marker="o", label="Clearwater River"), 
				 Line2D([0],[0], color="#cdcd00", marker="o", label="Dahler Lake",), 
				 Line2D([0],[0], color="#ffff00", marker="o", label="Decker Lake"), 
				 Line2D([0],[0], color="#00cd00", marker="o", label="Garfield Lake"), 
				 Line2D([0],[0], color="#00ff00", marker="o", label="Mud Hen Lake"), 
				 Line2D([0],[0], color="#00008b", marker="o", label="Necktie River"), 
				 Line2D([0],[0], color="#0000ff", marker="o", label="Ottertail River"), 
				 Line2D([0],[0], color="#cd3278", marker="o", label="Phantom Lake"), 
				 Line2D([0],[0], color="#ee82ee", marker="o", label="Plantagenet"), 
				 Line2D([0],[0], color="#541a8b", marker="o", label="Shell Lake"), 
				 Line2D([0],[0], color="#a020f0", marker="o", label="Upper Rice Lake")]

# Plot the legend
ax.legend(handles=legend_points, loc="center right")


fig.suptitle("Northern Wild Rice Collection Sites", family="serif")
ax.axis("off") # turn off the axis

fig.savefig("map_export.png", dpi=300)