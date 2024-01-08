import logging
import time
import signal
import os
import sys

from flask import Flask

from app_logs.app_logger import Logger
from worker import Worker

logger = Logger().get()
logger.info("Version 0.1")


MAIN_PID = None
SUB_PID = None
"""
    Docker sends SIGTERM on stop, after 10 sec it sends kill
"""
def handler_stop_signals(signum, frame):
    logger.info("Got Signal:" + str(signum)+ " " + str(frame))
    logger.info("The SIGTERM(15) signal is a generic signal used to terminate a program. SIGTERM provides an elegance way to kill program")
    time.sleep(2)
    logger.info("Starting to stop, throw exception to main for clean up")
    raise KeyboardInterrupt()

# signal.signal(signal.SIGINT, handler_stop_signals) # (SIGINT): interrupt the session from the dialogue station
signal.signal(signal.SIGTERM, handler_stop_signals) # (SIGTERM): terminate the process in a soft way
# https://stackabuse.com/handling-unix-signals-in-python/



if __name__ == "__main__":
    logger.info("In main")
    wo = Worker()
    work = True
    try:
         MAIN_PID = os.getpid()
         pid = "Main Pid: " + str(MAIN_PID)
         logger.info(pid)
         while work:
             wo.do_work()
    except (KeyboardInterrupt, SystemExit) as ex:
        work = False
        logger.info("Stop command recieved")
        time.sleep(1)
        logger.info("Cleaning up")
        logger.info("Stopped, bye, bye")
        sys.exit(0)