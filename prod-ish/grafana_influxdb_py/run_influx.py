from influxdb import InfluxDBClient
user = "adminuser"
cred = "adminpassword"
client = InfluxDBClient(host="172.27.0.2", port=8086, username=user, password=cred)
print(client)
client.create_database("pyexample")

json_body = [
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2024-03-26T8:01:00Z",
        "fields": {
            "duration": 127
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2024-03-26T8:04:00Z",
        "fields": {
            "duration": 132
        }
    }

]

rv = client.write_points(json_body)
print(str(rv))