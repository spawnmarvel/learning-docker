# Python-bolierplate with Portainer

# Portainer

https://docs.portainer.io/start/install-ce/server/docker/linux


## Recall this old stuff

Lets copy some code from the old repos and make two containers.

* Python
* Portainer

https://follow-e-lo.com/2020/02/10/docker-ubuntu/

https://github.com/spawnmarvel/test_docker/blob/master/docker-compose.yml

We will use the while true add the requirements.txt and re factor a bit.

Lets take the app_logs and app_expetions also.

# Build and test it

Note.

Portainer Community Edition (CE) is a lightweight platform that effortlessly delivers containerized applications.

```bash
portainer/portainer-ce:latest

# copy python-boilerplate project to folder appdir
mkdir appdir

cp python-bolierplate

python-bolierplate$ cp Dockerfile app.py app_logger.py logging_config.ini worker.py ../appdir/

```
Edit code

```py

# add a while loop to app.py
 while work:
             wo.do_work()
# edit worker.py
    def do_work(self):
        time.sleep(2)
        logger.info("Sleeping....")
        

```


https://hub.docker.com/r/portainer/portainer-ce

# Docker compose




