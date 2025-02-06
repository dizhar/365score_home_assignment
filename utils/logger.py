import logging
from  utils.config import Config


class Logger:
    LOG_FILE = Config.LOG_FILE

    def __init__(self):
        self.logger = logging.getLogger("QA_Automation")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.LOG_FILE)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
