# Image Management Concepts & Notes

> Find the full information about different layers that constitute the image

`docker history <image-name>:<tag-name>`

> Find the low level contents of an image

`docker inspect <image-name>:<tag-name>`

> Find out the layers that comprise a docker image

`docker inspect <image-name>:<tag-name> --format "{{.RootFS.Layers}}"`

> Save a docker image as tar file

`docker save <image-name>:<tag-name> > my-image.tar`

> Create a docker image without pulling from registry

`docker load < my-image.tar`

> Create a docker image on filesystem by importing the tar file

`docker import -m "my first image" my-image.tar`
