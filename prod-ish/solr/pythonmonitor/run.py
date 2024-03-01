import requests
import json

from pyzabbix import ZabbixMetric, ZabbixSender

def get_all():
    try:
        r = requests.get("http://20.162.161.241:8983/solr/gettingstarted/select?q=*:*")
        print("Solr status " + str(r.status_code))
        js = r.json()
        # print(js)
        li = js["response"]
        print(li["numFound"])
        metrix = li["numFound"]
        # for k, v in js.items():
            # print(k)
            # print(v)
            # print("\n")
        send_to_zabbix(metrix)
        return li
    except Exception as ex:
        print(ex)
    
def send_to_zabbix(metrix):
    try:
        metrics = []
        m = ZabbixMetric('VMSOLR', 'docs', metrix)
        metrics.append(m)
        zbx = ZabbixSender('51.145.42.219')
        zbx.send(metrics)
        print("sent to zabbix " + str(metrix))
    except Exception as ex:
        print(ex)


get_all()