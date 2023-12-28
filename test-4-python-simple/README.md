# Python-simple

# 101

```bash

python3
# Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux

mkdir python-simple
cd python simple

touch app.py Dockerfile

sudo nano app.py

```
app.py

```py
print("Hello Python")
```

Docker file

```bash

sudo nano Docker

FROM python:3.10-slim-buster
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./app.py" ]

```
Build it

```bash
pwd
/home/imsdal/python-simple

docker image build -t hello-py .
# This will use the Dockerfile to create an image tagged (-t) with a repository name of ‘hello-py’ using the current working directory (.). 
# The new image is based on the offical python:3.10-slim-buster image, has its working directory set to /usr/src/app, has both files copied into this directory and its default executable set to ‘python app.py’.



```

Run it

```bash
cd
pwd
# home/username

docker run hello-py
Hello  Python

```

Update the code

* cd to folder
* edit app.py

```bash
docker images

REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-py      latest    6040d71a596b   5 minutes ago   118MB
mariadb       11.0      2103f67114de   6 days ago      404MB
hello-world   latest    d2c94e258dcb   7 months ago    13.3kB

# try remove
docker rmi 6040d71a596b

# --force
docker rmi 6040d71a596b --force

# gone
docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
mariadb       11.0      2103f67114de   6 days ago     404MB
hello-world   latest    d2c94e258dcb   7 months ago   13.3kB

# build 
cd python-simple

docker image build -t hello-py .

# Run it
docker run hello-py

Hello  Python
A new line



````


https://medium.com/swlh/python-docker-the-basics-581f17132398

