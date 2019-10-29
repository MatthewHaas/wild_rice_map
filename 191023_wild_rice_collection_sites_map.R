# 23 October 2019
# WD: /home/jkimball/haasx092/collection_map

# The purpose of this code is to make an updated map (using an updated version of the sample collection file).
# Samples are colored according to the same colors as in the recently-completed PCA plots.

# Load required packages
library(data.table)
library(maps)

# Read in data
# Updated and corrected GPS coordinates. Confirmed with Tony Kern and Mingqin (Mike) Shao
x <- fread("191029_wild_rice_samples.csv")

# Make the figure
#pdf("191023_wild_rice_collection_sites.pdf")
pdf("191029_wild_rice_collection_sites.pdf")
map("state", xlim=c(-98, -89), ylim=c(42,50))
# Add major lakes
map("lakes", col="light blue", fill=TRUE, add=TRUE)
map("rivers", col=4, add=TRUE) # This is not working.. a different package needed?

points(x=x$Long, y=x$Lat, pch=16, col=x$col)

# There is no legend because the colors are meant to be interpreted based on the same color scheme as the PCA plots
legend("bottomright", legend=c("Aquatica species", "Bass Lake", "Big Fork River", "Clearwater River", "Dahler Lake",
"Decker Lake", "Garfield Lake", "Mud Hen Lake", "Necktie River", "Ottertail River", "Phantom Lake", "Plantagenet",
"Shell Lake", "Upper Rice Lake"), pch=16, col = x$col, cex=0.8, bg="white")

title("Wild Rice Collection Sites")

# Cities (I did not like how the built-in cities looked)
# St. Paul: -93.09, 44.95
points(-93.09, 44.95, pch=17)
text(-94, 44.95, labels="St. Paul")
# Duluth: -92.10, 46.79
points(-92.10, 46.79, pch=17)
text(-92.8, 46.9, labels="Duluth")
# Fargo: -96.79, 46,88
points(-96.8, 46.9, pch=17)
text(-97.5,46.9, labels="Fargo")


# Add a scale bar
map.scale(x=-96, y= 43, relwidth=0.15, metric=TRUE, ratio=FALSE, cex=0.7)
dev.off()
