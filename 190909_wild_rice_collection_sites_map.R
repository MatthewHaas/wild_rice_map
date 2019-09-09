# 09 September 2019
# An update to the map of collection sites for wild rice
# WD: /home/jkimball/haasx092/collection_map

library(data.table)
library(maps)

fread("190909_wild_rice_samples.csv") -> x

pdf("out.pdf")
map("state", xlim=c(-98, -89), ylim=c(42,50))
# Add major lakes
map("lakes", col="light blue", fill=TRUE, add=TRUE)
map("rivers", col=4, add=TRUE)

points(x=x$Long, y=x$Lat, pch=16, col=x$col)

# 2007 and 2009 collection sites do not have GPS coordinates. Should try to estimate based on lake/county. (For now they are excluded)
legend("topright", legend=c("2010", "2011", "2012", "2018"), pch=16, col=c(4,5,6,1), bty='n')
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
# Commenting out Bemidji because of the collection sites are obscured by the text


# Add a scale bar
map.scale(x=-96, y= 43, relwidth=0.15, metric=TRUE, ratio=FALSE, cex=0.7)
dev.off()