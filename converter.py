import json
import csv

json_file = input("Enter JSON file name: ")
csv_file = input("Enter output CSV file name: ")

try:
    with open(json_file, "r") as jf:
        data = json.load(jf)

    if isinstance(data, list) and len(data) > 0:
        keys = data[0].keys()

        with open(csv_file, "w", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print("Conversion successful.")

    else:
        print("Invalid JSON format (expected list of objects).")

except FileNotFoundError:
    print("JSON file not found.")
