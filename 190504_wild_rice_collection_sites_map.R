# 4 May 2019
# Making a map of Minnesota to show collection sites

# Install the US map package into a personal library
# It is first necessary to make the personal library on the command line (mkdir ~/R_libs)
install.packages("usmap", repos="http://cran.r-project.org", lib="~/R_libs/")

library(usmap)

library(maps)

pdf("190509_wild_rice_collection_sites.pdf")
# Things to fix: 1) see if islands can be colored white, 2) plot natural range of wild rice or cultivated regions?, 3) not all old samples are from 2008.. check original file for actual collection year
# Focus on Midwest region
map("state", xlim=c(-98, -89), ylim=c(42,50))
# Add major lakes
map("lakes", col="light blue", fill=TRUE, add=TRUE)
map("rivers", col=4, add=TRUE)

# Read in sample collection data (contains GPS coordinates)
fread("190509_2018_wild_rice_samples.csv") -> x

points(x=x$Long, y=x$Lat, pch=x$pch, col="green4")

legend("topright", legend=c("2008", "2018"), pch=c(0,1), col=c("green4"), bty='n')
title("Wild Rice Collection Sites")

# Cities (I did not like how the built-in cities looked)
# St. Paul: -93.09, 44.95
points(-93.09, 44.95, pch=16)
text(-94, 44.95, labels="St. Paul")
# Duluth: -92.10, 46.79
points(-92.10, 46.79, pch=16)
text(-92.8, 46.9, labels="Duluth")
# Fargo: -96.79, 46,88
points(-96.8, 46.9, pch=16)
text(-97.5,46.9, labels="Fargo")
# Commenting out Bemidji because of the collection sites are obscured by the text
# Bemidji: -94.88, 47.47
#points(-94.9, 47.5, pch=16)
#text(-94.7, 47.7, labels="Bemidji")

# Add a scale bar
map.scale(x=-96, y= 43, relwidth=0.15, metric=TRUE, ratio=FALSE, cex=0.7)
dev.off()
 