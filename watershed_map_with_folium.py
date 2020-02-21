# 21 February 2020
# Trying to make a better map of collection sites with Python
# WD: /home/jkimball/haasx092/collection_map

# Interatctive session
qsub -I -l nodes=1:ppn=4,mem=8gb,walltime=2:00:00 -q interactive

# Export commands need to be run on the command line
export PYTHONPATH=/home/jkimball/haasx092/.conda/
export PYTHONPATH=/home/jkimball/haasx092/.conda/pkgs/descartes-1.1.0-py_4/site-packages/descartes
export PYTHONPATH=/home/jkimball/haasx092/lib/python/

# Run this for folium (& geopandas)
python3 setup.py install --home=~

# Load python and launch an interactive version of python
module load python3
ipython

import folium
import pandas as pd
import json
from folium import plugins


MinnMap = folium.Map(location=[45, -94], titles="Minnesota", zoom_start=9)

MinnMap.save("MinnMap.html")