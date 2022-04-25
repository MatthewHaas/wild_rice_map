# 29 February 2020
# Updated: 24 September 2021
# Updated again: 7 January 2022
# Updated again: 25 April 2022 (plotting characters updated to reflect watershed)
# WD: /home/jkimball/haasx092/collection_map
# Code for plotting a map of Minnesota watersheds using geopandas
# Data come from Minnesota GIS: 

# Start an interactive python session (change wall time based on need)
#qsub -I -l nodes=1:ppn=4,mem=8gb,walltime=0:30:00 -q interactive

# Load python3
module load python3

# These should be run on the command line at the start of each session
export PYTHONPATH=/home/jkimball/haasx092/.conda/
export PYTHONPATH=/home/jkimball/haasx092/.conda/pkgs/descartes-1.1.0-py_4/site-packages/descartes
# export PYTHONPATH=/home/jkimball/haasx092//local/src/Cartopy/lib/cartopy ### not currently working
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
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib_scalebar.scalebar import SI_LENGTH
#import cartopy as ccrs # for scale bar

# The original shape file (watersheds) only contains the watersheds for Minnesota
# With the help of the Wisconsin DNR, I have separate shape files from both states using the Universal Transverse Mercator projection
# The "UTM15" refers to the zone they are in; technically WI is in both, but the person who helped me at the Wisconsin DNR set these up for me.
# The original code containing the path to the watershed has been commented out so it isn't functional but is still visible for future reference
# watersheds = "dnr_watersheds/dnr_watersheds_dnr_level_02_huc_04.shp"
wi = 'MN_WI_HUC4_WGS84_UTM15/WI_HUC4_WGS84_UTM15.shp'
mn = 'MN_WI_HUC4_WGS84_UTM15/MN_HUC4_WGS84_UTM15.shp'

collection_sites = "200224_wild_rice_samples.csv" # This updated file has GPS coordinates converted to Universal Transverse Mercator (UTM) format

#map_watersheds = gpd.read_file(watersheds) # read in watersheds (commented out but retaining for future references)
# Read in separate MN and WI watershed files
mn_dat = gpd.read_file(mn)
wi_dat = gpd.read_file(wi)
nwr_sites = pd.read_csv(collection_sites) # read in collection sites

# Combine (concatenate) separate MN and WI watershed files
map_watersheds = gpd.GeoDataFrame(pd.concat([mn_dat, wi_dat]))

# This section is for converting the latitude and longitude data into a form recognizable to geopandas
# The issue with the original projection issue is that the latitude and longitude needed to be converted to UTM format. I did the conversion of GPS coordinates with an online tool and created new columns in the CSV file containing the sample collection data.
def make_point(row):
    return Point(row.UTM_easting, row.UTM_northing) # Point() requires shapely.geometry

points = nwr_sites.apply(make_point, axis=1)
nwr_points = gpd.GeoDataFrame(nwr_sites, geometry=points)

# Not a very elegant approach, but this is how I think I need to go about plotting unique colors for each lake
aquatica = nwr_points[nwr_points.Location == "Aquatica_species"]
bass = nwr_points[nwr_points.Location == "Bass Lake"]
#bigfork = nwr_points[nwr_points.Location == "Big Fork River"]
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
ncroc = nwr_points[nwr_points.Location == "NCROC"]

# Start the plotting
fig, ax = plt.subplots(1, figsize=(20,15))
map_watersheds.plot(color="white", linewidth=1.0, ax=ax, edgecolor="black")
aquatica.plot(marker="^", markersize=75, ax=ax, color="#cd0000" ) # Aquatica
bass.plot(marker="o", markersize=75, ax=ax, color="#ff0000") # Bass Lake
clearwater.plot(marker="s", markersize=75, ax=ax, color="#ffa600") # Clearwater River
dahler.plot(marker="o", markersize=75, ax=ax, color="#cdcd00") # Dahler Lake
decker.plot(marker="o", markersize=75, ax=ax, color="#ffff00") # Decker Lake
garfield.plot(marker="o", markersize=75, ax=ax, color="#00cd00") # Garfield Lake
mudhen.plot(marker="D", markersize=75, ax=ax, color="#00ff00") # Mud Hen Lake
necktie.plot(marker="o", markersize=75, ax=ax, color="#00008b") # Necktie River
ottertail.plot(marker="s", markersize=75, ax=ax, color="#0000ff") # Ottertail River
phantom.plot(marker="D", markersize=75, ax=ax, color="#cd3278") # Phantom Lake
plantagenet.plot(marker="o", markersize=75, ax=ax, color="#ee82ee") # Plantagenet
shell.plot(marker="o", markersize=75, ax=ax, color="#541a8b") # Shell Lake
upperrice.plot(marker="s", markersize=75, ax=ax, color="#a020f0") # Upper Rice Lake
ncroc.plot(marker="*", markersize=250, ax=ax, color="black")

# Generate info for legend
legend_points = [Line2D([0],[0], color="#cd0000", marker="^", markersize=25, linestyle="none", label="$\it{Z. aquatica}$"), 
				 Line2D([0],[0], color="#ff0000", marker="o", markersize=25, linestyle="none", label="Bass Lake"),  
				 Line2D([0],[0], color="#ffa600", marker="s", markersize=25, linestyle="none", label="Clearwater River"), 
				 Line2D([0],[0], color="#cdcd00", marker="o", markersize=25, linestyle="none", label="Dahler Lake",), 
				 Line2D([0],[0], color="#ffff00", marker="o", markersize=25, linestyle="none", label="Decker Lake"), 
				 Line2D([0],[0], color="#00cd00", marker="o", markersize=25, linestyle="none", label="Garfield Lake"), 
				 Line2D([0],[0], color="#00ff00", marker="D", markersize=25, linestyle="none", label="Mud Hen Lake"), 
				 Line2D([0],[0], color="#00008b", marker="o", markersize=25, linestyle="none", label="Necktie River"), 
				 Line2D([0],[0], color="#0000ff", marker="s", markersize=25, linestyle="none", label="Ottertail River"), 
				 Line2D([0],[0], color="#cd3278", marker="D", markersize=25, linestyle="none", label="Phantom Lake"), 
				 Line2D([0],[0], color="#ee82ee", marker="o", markersize=25, linestyle="none", label="Plantagenet"), 
				 Line2D([0],[0], color="#541a8b", marker="o", markersize=25, linestyle="none", label="Shell Lake"), 
				 Line2D([0],[0], color="#a020f0", marker="s", markersize=25, linestyle="none", label="Upper Rice Lake"),
				 Line2D([0],[0], color="black", marker="*", markersize=25, linestyle="none", label="NCROC")]

# Plot the legend
ax.legend(handles=legend_points, loc="lower right", facecolor="white", prop={"size":20}) # I thought facecolor would make background white vs. partially transparent. Maybe I'm using it wrong?

# Define scalebar
scalebar = ScaleBar(dx=1, units="m", dimension=SI_LENGTH, location="lower center", pad=-2, font_properties="Times-30")

# Add scale bar
ax.add_artist(scalebar)

# If you want to re-add the title, remove the pound symbol (#) from the next line (it was commented out for publication)
#fig.suptitle("Nothern Wild Rice Collection Sites\nBy Watershed", family="serif")
ax.axis("off") # turn off the axis

fig.savefig("watershed_map_export.png", dpi=300)
