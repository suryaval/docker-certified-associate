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

