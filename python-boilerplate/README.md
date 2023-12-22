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





