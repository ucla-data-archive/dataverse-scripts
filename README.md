# Library List
Available through pip
- pyDataverse https://pypi.org/project/pyDataverse/
- PyShp / shapefile https://pypi.org/project/pyshp/ 
- laspy https://pypi.org/project/laspy/
- pdal https://pypi.org/project/PDAL/


# Notebooks 

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
- **shapefile**  PyShp
- json

## readLidarFolder
Reads though a folder of .las files (right now just 2) and makes a list with the filename and x and y, min and max boundries
 Not sure if this is correct for bounding box   
 - **laspy**
 - numpy
 - glob

## geopackage 1.0.0  
- A package to read/write GeoPackage Vector Data
- pip install geopackage

## geopackage-python  
- https://pypi.org/project/geopackage-python/  
- This one is set of tools for creating geopackages

## getDatasetInfo
examples of pyDataverse pulling dataset information, dataset dict structure
- ##pyDataverse**
- pandas
- json
- pprint < so you can print out the dictionary structure, visually helpful
- os

## dataverse_upload_file.ipynb  
Single file upload works on regular dataverse s3 bucket BUT not on the direct-upload s3 bucket

## prototype-create-list-then-upload.ipynb  
blocking out how the actual upload program would work
