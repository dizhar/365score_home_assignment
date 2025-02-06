import random
import allure
import logging
from utils.api_client import APIClient

logger = logging.getLogger(__name__)

@allure.feature("Create Post")
@allure.story("Verify successful post creation")
def test_create_post():
    api = APIClient()

    with allure.step("Retrieve a list of users"):
        user_response = api.get("/users")
        assert user_response.status_code == 200, 201
        users = user_response.json()
        assert users, "User list is empty"

    with allure.step("Select a random user"):
        user = random.choice(users)
        user_id = user["id"]

    with allure.step(f"Create a post for User ID {user_id}"):
        post_data = {
            "userId": user_id,
            "title": "Automated Test Post",
            "body": "This is a test post created via API."
        }
        post_response = api.post("/posts", post_data)
        assert post_response.status_code in [200, 201], f"Unexpected status code: {post_response.status_code}"

        response_data = post_response.json()
        assert response_data["title"] == post_data["title"]
        assert response_data["body"] == post_data["body"]

    logger.info(f"✅ Post successfully created for User ID {user_id}")
