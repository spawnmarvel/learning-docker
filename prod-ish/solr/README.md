# solr

## hub docker

https://hub.docker.com/_/solr

## Getting started with the Docker image

https://solr.apache.org/guide/solr/latest/deployment-guide/solr-in-docker.html#getting-started-with-the-docker-image

```bash

mkdir solrdev

cd solrdev

cp compose.yml

docker compose up -d


```

visit

http://xx.xx.xxx.xxx:8983/solr/#/gettingstarted/core-overview

Load it with date:


```bash
docker exec -it 7f186c0a9aa7  post -c gettingstarted example/exampledocs/manufacturers.xml
```

## Solr in Docker

https://solr.apache.org/guide/solr/latest/deployment-guide/solr-in-docker.html

## Python monitor (on windows)

```py
import requests
import json


def get_all():
    try:
        r = requests.get("http://xx.xxx.xxx.xxx:8983/solr/gettingstarted/select?q=*:*")
        print("Solr status " + str(r.status_code))
        js = r.json()
        li = js["response"]
        print(li["numFound"])
        return li
    except Exception as ex:
        print(ex)


get_all()

```
Result:

Solr status 200

11

```log
response
{'numFound': 11, 'start': 0, 'numFoundExact': True, 'docs': 
[{'id': 'adata', 'compName_s': 'A-Data Technology', 'address_s': '46221 Landing Parkway Fremont, CA 94538', '_version_': 1792350484097400832},
 {'id': 'apple', 'compName_s': 'Apple', 'address_s': '1 Infinite Way, Cupertino CA', '_version_': 1792350484142489600}, 
 {'id': 'asus', 'compName_s': 'ASUS Computer', 'address_s': '800 Corporate Way Fremont, CA 94539', '_version_': 1792350484143538176},
 {'id': 'ati', 'compName_s': 'ATI Technologies', 'address_s': '33 Commerce Valley Drive East Thornhill, ON L3T 7N6 Canada', '_version_': 1792350484144586752}, 
 {'id': 'belkin', 'compName_s': 'Belkin', 'address_s': '12045 E. Waterfront Drive Playa Vista, CA 90094', '_version_': 1792350484144586753}, 
 {'id': 'canon', 'compName_s': 'Canon, Inc.', 'address_s': 'One Canon Plaza Lake Success, NY 11042', '_version_': 1792350484145635328}, 
 {'id': 'corsair', 'compName_s': 'Corsair Microsystems', 'address_s': '46221 Landing Parkway Fremont, CA 94538', '_version_': 1792350484145635329},
 {'id': 'dell', 'compName_s': 'Dell, Inc.', 'address_s': 'One Dell Way Round Rock, Texas 78682', '_version_': 1792350484146683904},
 {'id': 'maxtor', 'compName_s': 'Maxtor Corporation', 'address_s': '920 Disc Drive Scotts Valley, CA 95066', '_version_': 1792350484146683905},
 {'id': 'samsung', 'compName_s': 'Samsung Electronics Co. Ltd.', 'address_s': '105 Challenger Rd. Ridgefield Park, NJ 07660-0511', '_version_': 1792350484147732480}]}

```


## pip install offline

https://stackoverflow.com/questions/11091623/how-to-install-packages-offline

pip install py-zabbix

```cmd
# On a computer connected to the internet, create a folder.

cd c:\tenp

# open up a command prompt or shell and execute the following command

pip download py-zabbix
Collecting py-zabbix
  Downloading py_zabbix-1.1.7-py3-none-any.whl (19 kB)
Saved c:\users\jekl\py_zabbix-1.1.7-py3-none-any.whl
Successfully downloaded py-zabbix

dir

py_zabbix-1.1.7-py3-none-any.whl

# Now, on the target computer, copy the packages folder and apply the following command

c:\temp>pip install py_zabbix-1.1.7-py3-none-any.whl --no-index --find-links '.'
Looking in links: '.'
Processing .\py_zabbix-1.1.7-py3-none-any.whl
Installing collected packages: py-zabbix
Successfully installed py-zabbix-1.1.7

pip freeze

py-zabbix @ file:///C:/temp/py_zabbix-1.1.7-py3-none-any.whl#sha256=f921abc88298c56f5aab9054815122ca959f8612df88fdc3a240ad2d95e4c282



```

## Send to zabbix

```py
import requests
import json

from pyzabbix import ZabbixMetric, ZabbixSender

def get_all():
    try:
        r = requests.get("http://xx.xxx.xxx.xxx:8983/solr/gettingstarted/select?q=*:*")
        print("Solr status " + str(r.status_code))
        js = r.json()
        li = js["response"]
        print(li["numFound"])
        metrix = li["numFound"]
        send_to_zabbix(metrix)
        return li
    except Exception as ex:
        print(ex)
    
def send_to_zabbix(metrix):
    try:
        metrics = []
        m = ZabbixMetric('VMSOLR', 'docs', metrix)
        metrics.append(m)
        zbx = ZabbixSender('xx.xx.xx.xx')
        zbx.send(metrics)
        print("sent to zabbix " + str(metrix))
    except Exception as ex:
        print(ex)


get_all()

```

Example

![Solr monitor](https://github.com/spawnmarvel/learning-docker/blob/main/images/solr_monitor.jpg)

https://py-zabbix.readthedocs.io/en/latest/quickstart_guide.html


# NSSM









