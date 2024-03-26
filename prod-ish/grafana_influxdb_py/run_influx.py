import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import time

bucket = "myBucket"
org = "myOrg"
token = "randomTokenValue"
# Store the URL of your InfluxDB instance
url="http://172.27.0.2:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Write script
write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)
time.sleep(5)
p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 30.3)
write_api.write(bucket=bucket, org=org, record=p)
time.sleep(5)
p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 40.3)
rv = write_api.write(bucket=bucket, org=org, record=p
print(str(rv))