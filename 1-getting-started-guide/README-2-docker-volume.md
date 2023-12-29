# Docker volume

With the previous experiment, you saw that each container starts from the image definition each time it starts. While containers can create, update, and delete files, those changes are lost when you remove the container and Docker isolates all changes to that container. 

With volumes, you can change all of this.

Volumes provide the ability to connect specific filesystem paths of the container back to the host machine. 

If you mount a directory in the container, changes in that directory are also seen on the host machine. 

If you mount that same directory across container restarts, you'd see the same files.

There are two main types of volumes. You'll eventually use both, but you'll start with volume mounts.

https://docs.docker.com/storage/volumes/

## Example RabbitMQ

