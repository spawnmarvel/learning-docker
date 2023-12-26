# Python-boilerplate

## Continue from python-simple

* Add logging to file and config for log
* View the logs
* Some simple logic, 2 classes and a main file
* Add greacefully shutdown

```bash

mkdir python-boilerplate

cd python-simple

cp Docker app.py

cp Dockerfile app.py ../python-bolierplate/

# Now we have copied the files

```

## Add classes and config

* Add a class for logging, app_logger.py also add logging_config.ini
* Import it in app.py and make the main method
* Run the app

```bash
python3 app.py

```
Logs

```log
2023-12-22 20:24:47,663 - 140240290516992 - 1573 - app.py - 6 -             <module>() root - INFO - Version 0.1
Hello Python
2023-12-22 20:24:47,663 - 140240290516992 - 1573 - app.py - 11 -                 main() root - INFO - In main

```

```bash
ls

Dockerfile  __pycache__  app.py  app_logger.py  logging_config.ini  logs_app.txt

```

## Add Greacfull shutdown for Docker

So we update the main with a sleep loop.

Now lets add greacfull shutdown with SIGTERM.

```bash
python3 app.py

```
Logs and we send a ctrl+c in the middle

```log

2023-12-22 20:50:36,309 - 140403686789120 - 1714 - app.py - 11 -             <module>() root - INFO - Version 0.1
2023-12-22 20:50:36,309 - 140403686789120 - 1714 - app.py - 33 -             <module>() root - INFO - In main
2023-12-22 20:50:36,309 - 140403686789120 - 1714 - app.py - 39 -             <module>() root - INFO - Main Pid: 1714
2023-12-22 20:50:38,311 - 140403686789120 - 1714 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2023-12-22 20:50:40,314 - 140403686789120 - 1714 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2023-12-22 20:50:42,316 - 140403686789120 - 1714 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2023-12-22 20:50:44,319 - 140403686789120 - 1714 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2023-12-22 20:50:46,321 - 140403686789120 - 1714 - worker.py - 16 -              do_work() root - INFO - Sleeping....
2023-12-22 20:50:48,323 - 140403686789120 - 1714 - worker.py - 16 -              do_work() root - INFO - Sleeping....
^C
2023-12-22 20:50:49,810 - 140403686789120 - 1714 - app.py - 42 -             <module>() root - INFO - Stop command recieved
2023-12-22 20:50:50,812 - 140403686789120 - 1714 - app.py - 44 -             <module>() root - INFO - Cleaning up
2023-12-22 20:50:50,812 - 140403686789120 - 1714 - app.py - 45 -             <module>() root - INFO - Stopped, bye, bye


```

```bash
ls
Dockerfile  __pycache__  app.py  app_logger.py  logging_config.ini  logs_app.txt  worker.py
```

## Now make the docker container

```bash

# build 
cd python-boilerplate

docker image build -t python-boil .

# Run it
docker run python-boil

# and it startes to log

# stop it ctrl+ c

# view it
docker images

# remove it it
docker rmi 5c8089f9ef31 --force

```








