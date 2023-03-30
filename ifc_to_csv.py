import sys
import json
import ifcopenshell
import csv

def read_json_file(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def read_ifc_file(ifc_file_path):
    ifc_file = ifcopenshell.open(ifc_file_path)
    return ifc_file

def get_property_value(elem, prop_set_name, property_name):
    try:
        for rel in elem.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByProperties") and rel.RelatingPropertyDefinition.Name == prop_set_name:
                for prop in rel.RelatingPropertyDefinition.HasProperties:
                    if prop.Name == property_name:
                        return prop.NominalValue.wrappedValue if hasattr(prop, "NominalValue") else None
    except Exception:
        pass
    return None

def parse_ifc_data(ifc_file, elements_filter, properties_filter):
    data_matrix = []
    for item in ifc_file:
        if item.is_a() in elements_filter:
            row = {"Type": item.is_a(), "GlobalId": item.GlobalId}
            for prop_set_name, property_names in properties_filter.items():
                for property_name in property_names:
                    row[f"{prop_set_name}:{property_name}"] = get_property_value(item, prop_set_name, property_name)
            data_matrix.append(row)
    return data_matrix

def write_csv_file(csv_file_path, data):
    with open(csv_file_path, "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main(ifc_file_path, elements_filter_path, properties_filter_path, output_file_path):
    elements_filter = read_json_file(elements_filter_path)
    properties_filter = read_json_file(properties_filter_path)
    ifc_file = read_ifc_file(ifc_file_path)
    data_matrix = parse_ifc_data(ifc_file, elements_filter, properties_filter)
    write_csv_file(output_file_path, data_matrix)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python ifc_to_csv.py <input.ifc> <elements_filter.json> <properties_filter.json> <output.csv>")
        sys.exit(1)

    ifc_file_path = sys.argv[1]
    elements_filter_path = sys.argv[2]
    properties_filter_path = sys.argv[3]
    output_file_path = sys.argv[4]
    main(ifc_file_path, elements_filter_path, properties_filter_path, output_file_path)
