# Image-building best practices

https://docs.docker.com/get-started/09_image_best/

## Containerize an application

```bash
```


## Update the application

```bash
```


## Share the application

```bash
```



## Persist db

```bash
```

## Use bind mounts

```bash
```

## Multi container apps

```bash
```

## Use docker compose

```bash
# oh great I stopped here, nice.

pwd
# /home/imsdal/getting-started-app

ls
# Dockerfile  README.md  compose.yml  node_modules  package.json  spec  src  yarn.lock

docker compose up -d

# Network getting-started-app_default           Created                                                          
# Volume "getting-started-app_todo-mysql-data"  Created                                                          
# Container getting-started-app-mysql-1         Started                                                         
# Container getting-started-app-app-1           Started

# Open NSG 3000 again, it was rm'ed since I though I was done
# visit http://public-ip:3000



```

## and finally: Image-building best practice


Using the docker image history command, you can see the command that was used to create each layer within an image.

```bash
docker image history getting-started
# Error response from daemon: No such image: getting-started:latest
# we should get an output, But I have deleted the image
# Each of the lines represents a layer in the image. The display here shows the base at the bottom with the newest layer at the top. 
# Using this, you can also quickly see the size of each layer, helping diagnose large images.

# You'll notice that several of the lines are truncated. If you add the --no-trunc flag, you'll get the full output
docker image history --no-trunc getting-started

```

Layer caching

Now that you've seen the layering in action, there's an important lesson to learn to help decrease build times for your container images. 

Once a layer changes, all downstream layers have to be recreated as well.

Look at the following Dockerfile you created for the getting started app.

```bash
# syntax=docker/dockerfile:1
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
```
Going back to the image history output, you see that each command in the Dockerfile becomes a new layer in the image. 

You might remember that when you made a change to the image, the yarn dependencies had to be reinstalled. 

It doesn't make much sense to ship around the same dependencies every time you build.


To fix it, you need to restructure your Dockerfile to help support the caching of the dependencies. 

For Node-based applications, those dependencies are defined in the package.json file. 

You can copy only that file in first, install the dependencies, and then copy in everything else. 

Then, you only recreate the yarn dependencies if there was a change to the package.json.

```bash
# syntax=docker/dockerfile:1
FROM node:18-alpine
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
```

Create a file named .dockerignore in the same folder as the Dockerfile with the following contents.

node_modules

.dockerignore files are an easy way to selectively copy only image relevant files.

```bash
touch .dockerignore
sudo nano dockerignore
# add node_modules

ls
Dockerfile  README.md  compose.yml  node_modules  package.json  spec  src  yarn.lock

```
Build a new image

```bash
docker build -t getting-started .
```

You should see output like the following.

```log
[+] Building 34.9s (12/12) FINISHED                                                docker:default
 => [internal] load build definition from Dockerfile                                         0.0s
 => => transferring dockerfile: 181B                                                         0.0s
 => [internal] load .dockerignore                                                            0.1s
 => => transferring context: 53B                                                             0.0s
 => resolve image config for docker.io/docker/dockerfile:1                                   1.0s
 => [auth] docker/dockerfile:pull token for registry-1.docker.io                             0.0s
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:ac85f380a63b13dfcefa89046420  0.0s
 => [internal] load metadata for docker.io/library/node:18-alpine                            0.0s
 => [1/4] FROM docker.io/library/node:18-alpine                                              0.0s
 => [internal] load build context                                                            2.9s
 => => transferring context: 53.39MB                                                         2.9s
 => CACHED [2/4] WORKDIR /app                                                                0.0s
 => [3/4] COPY . .                                                                           7.4s
 => [4/4] RUN yarn install --production                                                     16.3s
 => exporting to image                                                                       6.4s
 => => exporting layers                                                                      6.3s
 => => writing image sha256:8e91c7a0ebe812a4d71f948ad2f05fd2888c4e7380f4be650c06ddf3a8ab899  0.0s
 => => naming to docker.io/library/getting-started
```

Now, make a change to the src/static/index.html file. For example, change the <title> to "The Awesome Todo App".

<title>Awesome Todo App</title>

Build it again

```bash
cd ..
cd ..
# must be where the Dockerfile is

docker build -t getting-started .
```

This time, your output should look a little different.

```log
[+] Building 26.2s (11/11) FINISHED                                                docker:default
 => [internal] load build definition from Dockerfile                                         0.0s
 => => transferring dockerfile: 181B                                                         0.0s
 => [internal] load .dockerignore                                                            0.0s
 => => transferring context: 53B                                                             0.0s
 => resolve image config for docker.io/docker/dockerfile:1                                   0.3s
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:ac85f380a63b13dfcefa89046420  0.0s
 => [internal] load metadata for docker.io/library/node:18-alpine                            0.0s
 => [1/4] FROM docker.io/library/node:18-alpine                                              0.0s
 => [internal] load build context                                                            0.2s
 => => transferring context: 452.32kB                                                        0.2s
 => CACHED [2/4] WORKDIR /app                                                                0.0s
 => [3/4] COPY . .                                                                           3.0s
 => [4/4] RUN yarn install --production                                                     16.4s
 => exporting to image                                                                       6.0s
 => => exporting layers                                                                      5.9s
 => => writing image sha256:6e9354cfb6610879bb516350ce653255b53a37d72b1c9e00bf69feec6b330af  0.0s
 => => naming to docker.io/library/getting-started
```
First off, you should notice that the build was much faster. 

And, you'll see that several steps are using previously cached layers. 

Pushing and pulling this image and updates to it will be much faster as well.






