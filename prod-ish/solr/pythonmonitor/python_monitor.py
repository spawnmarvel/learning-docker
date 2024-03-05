import http.client, urllib.parse
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
          self.solr_port = None
          self.solr_node = None
          self.solr_alias_zabbix = None
          self.metrics = None
          self.zabbix_host = None
          self.send_interval = None
          self.read_conf()
    
    def read_conf(self):
        try:
            with open("config.json") as json_file:
                data = json.load(json_file)
                self.solr_host = data["configuration"]["solr_host"]
                self.solr_port = data["configuration"]["solr_port"]
                self.solr_node = data["configuration"]["solr_node"]
                self.solr_alias_zabbix = data["configuration"]["solr_aliaszabbix"]
                self.metrics = data["configuration"]["metrics"] 
                self.zabbix_host = data["configuration"]["zabbix_host"]
                self.send_interval = data["configuration"]["send_interval"]
                logger.info(data)
        except Exception as ex:
            logger.error(ex)


    def get_solr_information(self):
        dict_data = {}
        try:
    
            temp_url_query = ('http://'+str(self.solr_host)+':8983/solr/'+str(self.solr_node)+'/select?q=*:*')
            logger.info(temp_url_query)
            # create connectio to server
            conn = http.client.HTTPConnection(self.solr_host, self.solr_port)
            # conn = http.client.HTTPConnection(self.solr_host,self.solr_port) # accepts a hostname, not url
            conn.request("GET",temp_url_query)

            response = conn.getresponse()
            logger.info(response)
            logger.info("Http status " + str(response.status))
            logger.info("Http reason " + str(response.reason))
            if response.status == 200:
                content_type = response.getheader("Content-Type")
                logger.info("Content type " + str(content_type))
                # Read the response content as bytes
                response_bytes = response.read()
                # Read the response content as a string (assuming it's text)
                response_text = response_bytes.decode("utf-8")
                logger.info("Lenght of response " + str(len(response_text)))
                # logger.debug(response_text)
                json_data = json.loads(response_text)


                temp_li = json_data["response"]
                for m in self.metrics:
                    logger.info(m)
                    metric_value = temp_li[m]
                    metric_key = m.lower()
                    dict_data[metric_key] = metric_value
            else:
                logger.info("Http status " + str(response.status))

            return dict_data
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
            dict_num = self.get_solr_information()
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
