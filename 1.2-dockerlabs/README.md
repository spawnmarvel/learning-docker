## dockerlabs

https://github.com/collabnix/dockerlabs?tab=readme-ov-file

## Docker for Beginner

Docker Image, Container, Dockerfile, Volumes, Networking


When you run a build, the builder attempts to reuse layers from earlier builds. 

If a layer of an image is unchanged, then the builder picks it up from the build cache. 

If a layer has changed since the last build, that layer, and all layers that follow, must be rebuilt.

```bash

FROM
WORKDIR
COPY
RUN download
COPY . .
RUN use the download
RUN
ENTRYPOINT ["PATH OR FILE", ARGS]
```

Dockerfile

* COPY index.html /usr/share/nginx/html/
* ADD http://www.vlsitechnology.org/pharosc_8.4.tar.gz 
* CMD ["top"]
* ENTRYPOINT ["/bin/echo", "Hi, your ENTRYPOINT instruction in Exec Form !"]
* WORKDIR /opt
* WORKDIR folder2
* RUN apk add --update 
* RUN apk add curl
* RUN rm -rf /var/cache/apk/
* ARG WELCOME_USER=Collabnix
* RUN echo "Welcome $WELCOME_USER, to Docker World!" > message.txt
* ENV WELCOME_MESSAGE="Welcome to Docker World"
* CMD ["sh", "-c", "echo $WELCOME_MESSAGE"]
* VOLUME /myvol
* EXPOSE 80/tcp
* LABEL version="1.0"
* ONBUILD RUN echo "You won't see me until later"

Healthcheck

* HEALTHCHECK --interval=30s --timeout=10s CMD curl -f http://localhost/ || exit 1


https://github.com/collabnix/dockerlabs/blob/master/workshop/docker/README.md

## Docker for Intermediate

Docker Compose, Swarm, Advanced Networking

## Docker for Advanced

Docker Security, Content Trust, Image Scanning, Swarm Mode Security
