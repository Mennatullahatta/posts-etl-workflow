import requests
import logging
import json

logging.basicConfig(level=logging.INFO)

def extract_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    logging.info(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        with open("extracted.json", "w") as f:
            json.dump(data, f)
        print(f"Extracted {len(data)} records.")
        return data
    else:
        raise Exception("API request failed")

if __name__ == "__main__":
    extract_data()

