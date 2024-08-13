# Prometheus

* Prometheus collects and stores its metrics as time series data, i.e. metrics information is stored with the timestamp at which it was recorded, alongside optional key-value pairs called labels.
* It is now a standalone open source project and maintained independently of any company. 



## Power your metrics and alerting with the leading open-source monitoring solution

* Data model, Prometheus fundamentally stores all data as time series
* Querying Prometheus, PromQL
* Grafana supports querying Prometheus and promethtus has built in expression browser
* Efficent storage, memory and local disk
* Simple operations, server is using local storage
* Precise alerting, Promql and alertmanager
* Many client libs
* Many integrations, docker etc.


https://prometheus.io/



## Features

* a multi-dimensional data model with time series data identified by metric name and key/value pairs
* PromQL, a flexible query language to leverage this dimensionality
* no reliance on distributed storage; single server nodes are autonomous
* time series collection happens via a pull model over HTTP
* pushing time series is supported via an intermediary gateway
* targets are discovered via service discovery or static configuration
* multiple modes of graphing and dashboarding support

https://prometheus.io/docs/introduction/overview/

## Docker

A sample Prometheus and Grafana stack.

https://docs.docker.com/samples/prometheus/


```bash
cd prometheus-grafana

docker compose up -d

# Network prometheus-grafana_default     Created                                                               
# Volume "prometheus-grafana_prom_data"  Created                                                                  
# Container grafana                      Started                                                                 
# Container prometheus                   Started


docker compose down
```

Navigate to http://localhost:3000 in your web browser and use the login credentials specified in the compose file to access Grafana. It is already configured with prometheus as the default datasource.

admin / grafana


Navigate to http://localhost:9090 in your web browser to access directly the web interface of prometheus.



## Python send data

```bash
pip install prometheus_client

```
```py
from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()

def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8888)
    # Generate some requests.
    while True:

        process_request(random.random())

```

Three: Visit http://localhost:8000/ to view the metrics.

From one easy to use decorator you get:

request_processing_seconds_count: Number of times this function was called.

request_processing_seconds_sum: Total amount of time spent in this function.

Prometheus’s rate function allows calculation of both requests per second, and latency over time from this data.


In addition if you’re on Linux the process metrics expose CPU, memory and other information about the process for free!

https://prometheus.github.io/client_python/getting-started/three-step-demo/


## TUTORIALS

### Getting Started with Prometheus

### Understanding metric types

### Visualizing metrics using Grafane

### Alert based on metric

https://prometheus.io/docs/tutorials/getting_started/


## INTRODUCTION

## CONCEPTS

## PROMETHEUS

## VISUALIZATION

## INSTRUMENTING

## OPERATING

## ALERTING

https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/

## BEST PRACTICES

## GUIDES

## Extra

How to Send Email Alerts using Prometheus AlertManager

https://blog.devops.dev/send-email-alerts-using-prometheus-alert-manager-16df870144a4



