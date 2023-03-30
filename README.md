# IFC-playground

this is a python script that takes two inputs: (1) It takes a list of ifc elements (e.g. IfcWall, IfcDoor) defined on "element_filter.json. (2) It takes a list of ifc properties (e.g. IfcWallCommon.ElementID) and then exports a matrix with all elements as rows and properties as columns.

To test it clone this repo and do the following:

python ifc_to_csv.py input.ifc elements_filter.json properties_filter.json output.csv

Change the input.ifc and output.csv as needed.  

100% done by ChatGPT
