import requests
import json


def get_all():
    r = requests.get("http://20.162.161.241:8983/solr/gettingstarted/select?q=*:*")
    print("Solr status " + str(r.status_code))
    js = r.json()
    # print(js)
    li = js["response"]
    print(li["numFound"])
    # for k, v in js.items():
        # print(k)
        # print(v)
        # print("\n")
    return li


get_all()