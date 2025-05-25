import csv
import logging
import json

logging.basicConfig(level=logging.INFO)

def load_data(filename="output.csv"):
    with open("transformed.json") as f:
        data = json.load(f)


    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "Count"])
        for user_id, count in data.items():
            writer.writerow([user_id, count])

    logging.info(f"Saved data to {filename}")


if __name__ == "__main__":
    load_data()
