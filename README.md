# IFC-playground

IFC-to-CSV: this is a python script that takes three inputs: (1) It takes a list of ifc elements (e.g. IfcWall, IfcDoor) defined in "element_filter.json. (2) It takes a list of ifc properties (e.g. IfcWallCommon.ElementID). (3) It takes an ifc file and then exports a matrix with all elements as rows and properties as columns.

Usage: "python ifc_to_csv.py <input.ifc> <elements_filter.json> <properties_filter.json> <output.csv>

Extract properties: extracts all properties from building elements of an ifc into a json-file.

Usage: "python generate_properties_filter.py <input.ifc> <elements_filter.json> <properties_filter.json>

100% done by ChatGPT
