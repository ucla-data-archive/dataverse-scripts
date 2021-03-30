# dataverse-scripts  

- Scripts for processing geospatial files for dataverse 
- Scripts for pre-processing geospatial files for the bounding-box/extent data  

For now I'm using jupyter notebooks to work out the scripts.
All libraries can be added with pip

## get_lariac_info.ipynb  
creates a csv of the files currently in the lariac4 folder,  these happen to be .las files

- **pyDataverse**
- datetime
- os
- pprint

## readshapefile
pulls bounding box information from shapefiles
right now just reads a hardcoded file but will change to read a directory
- **shapefile** 
- json

## readLidarFolder
Reads though a folder of .las files (right now just 2) and makes a list with
 - filename
 - x and y, min and max boundries
 Not sure if this is correct for bounding box
 
 - **laspy**
 - numpy
 - glob
