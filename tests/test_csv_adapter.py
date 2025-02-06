import allure
import pytest
from utils.csv_adapter import CSVAdapter

@allure.feature("Data-Driven Testing")
@allure.story("Verify API with multiple test data entries")
@pytest.mark.parametrize("test_data", CSVAdapter("test_data.csv").read_data())
def test_post_creation(test_data, api_client):
    """Test creating posts using data from CSV"""
    user_id = int(test_data["user_id"])
    title = test_data["title"]
    body = test_data["body"]

    with allure.step(f"Create a post for User ID {user_id}"):
        post_data = {"userId": user_id, "title": title, "body": body}
        post_response = api_client.post("/posts", post_data)
        assert post_response.status_code in [200, 201]
