import logging
import json 

logging.basicConfig(level=logging.INFO)

def transform_data(data):
    
    result = {}
    for item in data:
        user_id = item['userId']
        result[user_id] = result.get(user_id, 0) + 1

    logging.info(f"Transformed {len(data)} entries into {len(result)} categories")
    return result


if __name__ == "__main__":
    with open("extracted.json") as f:
        data = json.load(f)
    transformed = transform_data(data)
    with open("transformed.json", "w") as f:
        json.dump(transformed, f)
