import requests
from utils.logger import Logger
from utils.config import Config 

class APIClient:
    BASE_URL = Config.BASE_URL

    def __init__(self):
        self.session = requests.Session()
        self.logger = Logger().get_logger()

    def get(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        self.logger.info(f"GET {url}")
        response = self.session.get(url)
        self.logger.info(f"Response: {response.status_code} {response.text}")
        return response

    def post(self, endpoint, data):
        url = f"{self.BASE_URL}{endpoint}"
        self.logger.info(f"POST {url} | Data: {data}")
        response = self.session.post(url, json=data)
        self.logger.info(f"Response: {response.status_code} {response.text}")
        return response
