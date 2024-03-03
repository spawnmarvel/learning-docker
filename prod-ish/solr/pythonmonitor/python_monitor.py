import requests
import json
import time
import signal
import os
import sys

from pyzabbix import ZabbixMetric, ZabbixSender

from app_logs.app_logger import Logger

logger = Logger().get()



class PythonMonitor():

    def __init__(self):
        self.solr_host = None
        self.solr_node = None
        self.zabbix_host = None
        self.heartbeat_sec = None
    
    def read_conf(self):
        try:
            with open("config.json") as json_file:
                data = json.load(json_file)
                self.solr_host = data["configuration"]["solr_host"]
                self.solr_node = data["configuration"]["solr_node"]
                self.solr_alias_zabbix = data["configuration"]["solr_aliaszabbix"]
                self.zabbix_host = data["configuration"]["zabbix_host"]
                self.send_interval = data["configuration"]["send_interval"]
                logger.info("Node: " + str(self.solr_node))
                logger.debug(data)
        except Exception as ex:
            logger.error(ex)


        
    def get_num_docs(self):
        try:
            temp_url = ('http://' + str(self.solr_host) +  ':8983/solr/gettingstarted/select?q=*:*')
            r = requests.get(temp_url)
            logger.info("Solr status code: " + str(r.status_code))
            js = r.json()
            temp_li = js["response"]
            print(temp_li["numFound"])
            metrix_value = temp_li["numFound"]
            metrix_key = "docs"
            dict = {metrix_key: metrix_value}
            return dict
        except Exception as ex:
            logger.error(ex)
    
    def send_to_zabbix(self, metrix_key, metrix_value):
        try:
            metrics = []
            h = str(self.solr_alias_zabbix)
            m_k = str(metrix_key)
            m_v = str(metrix_value) 
            m = ZabbixMetric(h, m_k, m_v)
            metrics.append(m)
            zbx = ZabbixSender(str(self.zabbix_host))
            zbx.send(metrics)
            temp_sent = h + " " + m_k + " " + m_v
            logger.info("Sent to zabbix: "+ temp_sent)
        except Exception as ex:
            logger.error(ex)


    def start_monitor(self):
        try:
            self.read_conf()
            dict_num = self.get_num_docs()
            logger.info(dict_num)
            for k, v in dict_num.items():
                self.send_to_zabbix(k, v)
        except Exception as ex:
            logger.error(ex)
    

def main():
    while True:
        logger.info("Monitor started")
        py_mon = PythonMonitor()
        py_mon.start_monitor()
        logger.info("Sleep for: " + str(py_mon.send_interval))
        time.sleep(py_mon.send_interval)


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
    try:
        MAIN_PID = os.getpid()
        pid = "Main Pid: " + str(MAIN_PID)
        logger.info(pid)
        work= True
        while work:
            logger.info("Monitor started")
            py_mon = PythonMonitor()
            py_mon.start_monitor()
            logger.info("Sleep for: " + str(py_mon.send_interval))
            time.sleep(py_mon.send_interval)
    except (KeyboardInterrupt, SystemExit) as ex:
        work = False
        logger.info("Stop command recieved")
        time.sleep(1)
        logger.info("Shuting down")
        logger.info("Stopped, bye, bye")
        sys.exit(0)
