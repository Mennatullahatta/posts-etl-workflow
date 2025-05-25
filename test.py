from unittest.mock import patch
from extract import extract_data
from transform import transform_data

@patch('extract.requests.get')
def test_api_response(mock_get):
    # Mock the API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"userId": 1, "id": 1, "title": "title1", "body": "body1"},
        {"userId": 2, "id": 2, "title": "title2", "body": "body2"},
        {"userId": 1, "id": 3, "title": "title3", "body": "body3"},
    ]
    data = extract_data()
    assert isinstance(data, list)
    assert len(data) > 0

def test_transformation():
    sample_data = [
        {"userId": 1, "id": 1},
        {"userId": 2, "id": 2},
        {"userId": 1, "id": 3},
    ]
    transformed = transform_data(sample_data)
    assert transformed[1] == 2
    assert transformed[2] == 1


 





