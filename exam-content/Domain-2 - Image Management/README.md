# ​Image​ ​Creation,​ ​Management,​ ​and​ ​Registry​
(20%​ ​of​ ​exam) Content may include the following:

#### Describe Dockerfile options [add, copy, volumes, expose, entrypoint, etc)
https://github.com/suryaval/docker-notes/blob/master/s1/s1e4.md

#### Show the main parts of a Dockerfile

https://github.com/suryaval/docker-notes/blob/master/s1/s1e4.md

#### Give examples on how to create an efficient image via a Dockerfile
>   Use multi-stage builds

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#use-multi-stage-builds

```
For example, if your build contains several layers, you can order them from the less frequently changed (to ensure the build cache is reusable) to the more frequently changed:

Install tools you need to build your application

Install or update library dependencies

Generate your application
```

#### Use CLI commands such as list, delete, prune, rmi, etc to manage images
>   Search
```
$ docker search nginx --filter "is-official=true"
NAME                DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
nginx               Official build of Nginx.                        9179                [OK]
kong                Open-source Microservice & API Management la…   210                 [OK]


```

#### Inspect images and report specific attributes using filter and format

>   Find the layers present in the image by formatting the docker inspect command

```
docker inspect nginx:alpine --format='{{json .RootFS.Layers}}'
["sha256:717b092b8c86356cf976d9c83fa6f0ea67f2bf3148a5bbb7e02026a5d3245e68","sha256:692d855fb28ef134014a1c75b07cdfc26ff919a1194ba1176d1d2d4a095a9865","sha256:1585039add0af6ccc446f727942bea65851ba3a17c428eb1e8753ee30868a667","sha256:ecbc53aebc2747bcf0f7b01a20b0d7a17552f274b0e61a70b5e6aff9d06addd4"]
```

#### Demonstrate tagging an image

>   Pull the image
```
$ docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
8e3ba11ec2a2: Pull complete
Digest: sha256:7043076348bf5040220df6ad703798fd8593a0918d06d3ce30c6c93be117e430
Status: Downloaded newer image for alpine:latest
```

>   Run the container
```
$ docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
8e3ba11ec2a2: Pull complete
Digest: sha256:7043076348bf5040220df6ad703798fd8593a0918d06d3ce30c6c93be117e430
Status: Downloaded newer image for alpine:latest
```

>   Commit the container
```
$ export IMAGE_SHA=`docker commit $CONTAINER_ID`
[manager3] (local) root@192.168.0.4 ~

$ echo $IMAGE_SHA
sha256:c2c11b8496607257571187649af4b22b8f9cb2d41d0094b12e6adb9e1fe450ae

$ docker image ls --no-trunc|grep $IMAGE_SHA
<none>              <none>              sha256:c2c11b8496607257571187649af4b22b8f9cb2d41d0094b12e6adb9e1fe450ae   About a minute ago   4.41MB
```

>   Tag the image that was just committed

```
$ docker tag $IMAGE_SHA surval/alpine
[manager3] (local) root@192.168.0.4 ~

$ docker images|grep surval/alpine
surval/alpine       latest              c2c11b849660        2 minutes ago       4.41MB
```

#### Utilize a registry to store an image

>   Login to dockerhub and push the image

```
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: surval
Password:
Login Succeeded
[manager3] (local) root@192.168.0.4 ~

$ docker push surval/alpine:latest
The push refers to repository [docker.io/surval/alpine]
73046094a9b8: Mounted from library/alpine
latest: digest: sha256:d2f011b4043823ef4f396e7be5ade274b64a3ed2daa5f096747f1a68b634dd6a size: 528
```

#### Display layers of a Docker image

`docker inspect nginx:alpine --format='{{json .RootFS.Layers}}'`

#### Apply a file to create a Docker image

`docker build -t .`

#### Modify an image to a single layer

https://docs.docker.com/develop/develop-images/multistage-build/

#### Describe how image layers work

```
FROM ubuntu:15.04
COPY . /app
RUN make /app
CMD python /app/app.py

Each instruction creates one layer:

FROM creates a layer from the ubuntu:15.04 Docker image.
COPY adds files from your Docker client’s current directory.
RUN builds your application with make.
CMD specifies what command to run within the container.
```

#### Deploy a registry (not architect)

```
$ docker run -d -p 5000:5000 --restart=always --name registry \
             -v `pwd`/config.yml:/etc/docker/registry/config.yml \
             registry:2
```
#### Configure a registry

https://docs.docker.com/registry/configuration/

#### Log into a registry

`docker login http://localhost:5000/myrepo`

#### Utilize search in a registry

`docker search localhost:5000/myrepo/kong`

#### Tag an image

`docker tag src-image localhost:5000/myrepo/src-image`

#### Push an image to a registry

`docker push localhost:5000/myrepo/src-image`

#### Sign an image in a registry

```
export DOCKER_CONTENT_TRUST=1
docker push <dtr-domain>/<repository>/<image>:<tag>
```

#### Pull an image from a registry
>   docker pull dockerhub.com/suryaval/protractor:latest

#### Describe how image deletion works
>   When an image is deleted, all layers comprising of it will be deleted

>   If an image is based upon another image, parent image will not be allowed to be deleted (except using -f) since child images are dependant on it

#### Delete an image from a registry
```
$ docker rmi deca91a2f909
Untagged: drone/drone@sha256:638e81bbb62c8521af4a7ad54ef5e4f457dbaa10e069ff3a180702d94be0a176
Deleted: sha256:deca91a2f90960d42ee06ba87ef6d3664d15827f907e784c1f8a835c1924d8c3
Deleted: sha256:51b8f87f1d7b37867e70e8d6b1318ce75db492fd5a96b8b5a90b905fd25e1e99
```
