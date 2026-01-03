import logging
import time
from app_logger import Logger


logger = Logger().get()

class Worker:

    def __init__(self):
        pass

    def do_work(self):
        time.sleep(2)
        logger.info("Sleeping long tomorrow....")
