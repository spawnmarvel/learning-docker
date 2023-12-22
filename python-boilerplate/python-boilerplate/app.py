import logging

from app_logger import Logger

logger = Logger().get()
logger.info("Version 0.1")


def main():
    print("Hello Python")
    logger.info("In main")

if __name__ == "__main__":
    main()