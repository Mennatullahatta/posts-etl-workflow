import json


try:
# Load the extracted data
    with open('extracted.json', 'r') as f:
        data = json.load(f)

    # Count the number of records
    if isinstance(data, list):
        print(f"Extracted {len(data)} records.")
    else:
        print("Extracted data is not a list.")


except FileNotFoundError:
    print("File 'extracted.json' not found.")
except json.JSONDecodeError:
    print("File 'extracted.json' is not valid JSON.")
