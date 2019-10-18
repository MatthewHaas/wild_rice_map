# wild_rice_map
Map of Minnesota showing collection sites for wild rice (_Zizania_ sp.). The idea is to use the map to show where the collection sites for Natural Stand material were harvested. Once we have population genetic strucutre, we could also color collection sites by population membership. Some of the material was also harvested in the 2008-2011 time frame, so there is an interesting temporal component to the collections.

## 190504_wild_rice_collection_sites_map.R
This is an older version of the R code that I used to make an initial/rough version of the figure.

Input:
  - GPS coordinates (190509_2018_wild_rice_samples.csv)

Output:
  - Map (190509_wild_rice_collection_sites.pdf)
  
## 190909_wild_rice_collection_sites_map.R
This is an updated version of the R code. It is very similar to the file **190504_wild_rice_collection_sites_map.R** but it has the correct years for older material. Aesthetic changes were also made to improve the appearance of the map.

Input:
  - GPS coordinates (190909_wild_rice_samples.csv)
  
Output:
  - Map (190909_wild_rice_collection_sites.pdf)
