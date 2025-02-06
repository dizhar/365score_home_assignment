import random
import allure
import logging
from utils.api_client import APIClient

logger = logging.getLogger(__name__)

@allure.feature("User Posts")
@allure.story("Verify user's posts contain valid Post IDs")
def test_get_user_posts():
    api = APIClient()

    with allure.step("Retrieve a list of users"):
        user_response = api.get("/users")
        assert user_response.status_code == 200, f"Unexpected status code: {user_response.status_code}"
        users = user_response.json()
        assert users, "User list is empty"

    with allure.step("Select a random user and get email"):
        user = random.choice(users)
        user_id = user["id"]
        user_email = user["email"]
        logger.info(f"Selected User ID: {user_id}, Email: {user_email}")
        assert "@" in user_email  # Simple validation
        allure.attach(f"User Email: {user_email}", name="User Email", attachment_type=allure.attachment_type.TEXT)

    with allure.step(f"Retrieve posts for User ID {user_id}"):
        posts_response = api.get(f"/posts?userId={user_id}")
        assert posts_response.status_code in [200, 201], f"Unexpected status code: {posts_response.status_code}"
        posts = posts_response.json()
        assert posts, f"No posts found for user ID {user_id}"

    with allure.step(f"Validate Post IDs for User ID {user_id}"):
        for post in posts:
            assert isinstance(post["id"], int), f"Post ID is not an integer: {post['id']}"
            assert 1 <= post["id"] <= 100, f"Post ID out of range: {post['id']}"

    logger.info(f"✅ Successfully validated {len(posts)} posts for User ID {user_id}")
