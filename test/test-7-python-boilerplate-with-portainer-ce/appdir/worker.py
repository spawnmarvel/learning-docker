import logging
import time
import json
from app_logger import Logger
from appdir import tools

logger = Logger().get()

class Worker:

    def __init__(self):
        pass

    def read_conf(self):
        try:
            with open("config.json", "r") as json_file:
                json_result = json.load(json_file)
                logger.info(json_result)
        except FileNotFoundError as ex:
            logger.error(ex)

    def do_work(self):
        time.sleep(2)
        logger.info("Sleeping....")
        self.read_conf()
