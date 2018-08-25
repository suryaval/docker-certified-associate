# Domain​ ​6:​ ​Storage​ ​and​ ​Volumes​
(10%​ ​of​ ​exam) Content may include the following: 

#### State which graph driver should be used on which OS
* CentOS: devicemapper
* Ubuntu: aufs3
* MacOS: overlay2
`docker info | grep Storage`
aufs, overlay - operate at file level
devicemapper, btrfs - operate at block level

#### Demonstrate how to configure devicemapper


#### Compare object storage to block storage, and explain which one is preferable when available


#### Summarize how an application is composed of layers and where those layers reside on the filesystem


#### Describe how volumes are used with Docker for persistent storage

`/etc/docker/volumes`

#### Identify the steps you would take to clean up unused images on a filesystem, also onDTR

`docker system prune`
removes all dangling images

#### Demonstrate how storage can be used across cluster nodes

`mount docker volume across all nodes or create volume and specify to be attached to each service on startup`
