# Essential Docker commands

To pull an image from hub.docker.com

>   docker image pull nginx

To find the location of docker images and other information about docker

>   docker system info

To find information about images along with their hash (SHA 256)

>   docker images --digests

To find the complete info about an image

>   docker image inspect redis

To delete the image

>   docker image rm redis

To pull a specific docker image from a registry

>   docker image pull docker.io/nginx/latest

To pull all images corresponding to a repo

>   docker image pull docker.io/nginx -a

To create an image out of Dockerfile ( considering Dockerfile is at current directory )

>   docker build -t <image-name> .

Run a docker container with the image built out of the Dockerfile

>   docker container run -d --name <image-name> -p 80:80 mywebsite

Stop at a specific build stage (using Dockerfile in multi-stage-Dockerfile)

>   docker build --target builder -t alexellis2/href-counter:latest

List all containers

>   docker container ls

Run a container out of a docker image

>   docker run -it <image-name> /bin/bash

List all containers (exited and active)

>   docker ps -a

Login into a running docker container

>   docker exec -it <container-name> /bin/bash

List the ports used by a container

>   docker port <container-name>

Remove all docker containers that are exited

>   docker rm $(docker ps -a -q) -f

Find the current logging driver

>   docker info|grep 'Loggin Driver'

## Swarm

Start a single node swarm

>   docker swarm init

>   docker swarm init --advertise-addr=<ip>

Get Join Token for manager

>   docker swarm join-token manager

Get Join Token for worker

>   docker swarm join-token worker

Rotate an existing swarm token

>   docker swarm join-token manager --rotate

>   docker swarm join-token worker --rotate

*   Swarm locking
    *   stops manager from automatically rejoining a swarm
    *   this helps from rotating the keys whenever required
    *   prevents restoring old copy of swarm

        >   docker swarm update --autolock

    *   The above command gives autolock key

        >   docker swarm unlock

    *   GIve the unlock key to unlock swarm
