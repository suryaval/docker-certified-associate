# Orchestration 
(25% of exam)
Content may include the following:

#### Complete the setup of a swarm mode cluster, with managers and worker nodes

```
$ docker swarm init --advertise-addr=192.168.0.8 

(default node becomes the only manager in the swarm)

Get join token for the manager

$ docker swarm join-token manager

Get join token for the worker

$ docker swarm join-token worker

Make a dockerized node the manager

$ docker swarm join --token SWMTKN-1-1y5y9aca6zj9gun4ln6gayqrrwg49fhw6m5b5q39tuyugopxmnj-21j4imgh9fed463gvpglyzypi 192.168.0.8:2377

Make a dockerized node the worker

$ docker swarm join --token SWMTKN-1-1y5y9aca6zj9gun4ln6gayqrrwawdfafhw6m5b5q39tu6hopxmnj-7ygrqs777mfulk0mennyq37jo 192.168.0.8:2377

$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
srqv7up1ttuq4w1cka1zv3fen *   node1               Ready               Active              Leader              18.03.1-ce
yxvxgz98ujxy2103goe61f7c6     node2               Ready               Active              Reachable           18.03.1-ce
x17qfaioznyaid479ef1rvxi5     node3               Ready               Active              Reachable           18.03.1-ce
radpqalrb3o9lfoli093o4h62     node4               Ready               Active                                  18.03.1-ce
obfsi8vw7tjarljcbgqxd2i3w     node5               Ready               Active                                  18.03.1-ce

```

#### State the differences between running a container vs running a service

>   Running a Service

```
$ docker service create --name redis redis:3.0.6
mnejoka8adtyb1vz6ejtw20ja
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged
```

>  Running a container

```
$ docker run -td --name redis-container redis:3.0.6
Unable to find image 'redis:3.0.6' locally
3.0.6: Pulling from library/redis
81cc5f26a6a0: Already exists
a3ed95caeb02: Already exists
d43cb752619e: Already exists
861e96e7ae14: Already exists
7fae3dcea8af: Already exists
b46c28ddbe0c: Already exists
2d50fb4bcfa7: Already exists
c8fc9e7dfb8b: Already exists
a1a961e320bc: Already exists
Digest: sha256:6a692a76c2081888b589e26e6ec835743119fe453d67ecf03df7de5b73d69842
Status: Downloaded newer image for redis:3.0.6
1dddbe5cc61bfe62df0b4eb73c5fb735b773ffefb477908cfe35bf71f58ef8af
[node1] (local) root@192.168.0.8 ~

$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
1dddbe5cc61b        redis:3.0.6         "/entrypoint.sh redi…"   8 seconds ago       Up 7 seconds        6379/tcp            redis-container
62c3c4aa18da        redis:3.0.6         "/entrypoint.sh redi…"   7 minutes ago       Up 7 minutes        6379/tcp            redis.1.ibquqh186v5sc58ev7bpulojc
```

#### Demonstrate steps to lock a swarm cluster

>   Initiate Swarm auto lock: 

    docker swarm update --autolock=true

>   Unlock a Swarm -- requires key to unlock:

    docker swarm unlock

#### Extend the instructions to run individual containers into running services under swarm

#### Interpret the output of "docker inspect" commands
```
$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
mnejoka8adty        redis               replicated          10/10               redis:3.0.6
[node1] (local) root@192.168.0.8 ~

$ docker service inspect redis
[
    {
        "ID": "mnejoka8adtyb1vz6ejtw20ja",
        "Version": {
            "Index": 150
        },
        "CreatedAt": "2018-08-04T20:40:13.803298638Z",
        "UpdatedAt": "2018-08-04T21:05:57.643565456Z",
        "Spec": {
            "Name": "redis",
            "Labels": {},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "redis:3.0.6@sha256:6a692a76c2081888b589e26e6ec835743119fe453d67ecf03df7de5b73d69842",
                    "StopGracePeriod": 10000000000,
                    "DNSConfig": {},
                    "Isolation": "default"
                },
                "Resources": {
                    "Limits": {},
                    "Reservations": {}
                },
                "RestartPolicy": {
                    "Condition": "any",
                    "Delay": 5000000000,
                    "MaxAttempts": 0
                },
                "Placement": {
                    "Platforms": [
                        {
                            "Architecture": "amd64",
                            "OS": "linux"
                        }
                    ]
                },
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 10
                }
            },
            "UpdateConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "RollbackConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "EndpointSpec": {
                "Mode": "vip"
            }
        },
        "PreviousSpec": {
            "Name": "redis",
            "Labels": {},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "redis:3.0.6@sha256:6a692a76c2081888b589e26e6ec835743119fe453d67ecf03df7de5b73d69842",
                    "DNSConfig": {},
                    "Isolation": "default"
                },
                "Resources": {
                    "Limits": {},
                    "Reservations": {}
                },
                "Placement": {
                    "Platforms": [
                        {
                            "Architecture": "amd64",
                            "OS": "linux"
                        }
                    ]
                },
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 1
                }
            },
            "EndpointSpec": {
                "Mode": "vip"
            }
        },
        "Endpoint": {
            "Spec": {}
        }
    }
]
```
#### Convert an application deployment into a stack file using a YAML compose file with "docker stack deploy"

https://github.com/suryaval/docker-notes/blob/master/s5/s5e1.md

#### Manipulate a running stack of services

>   Update the docker-stack.yaml and redeploy the stack. Only changed configurations will be picked up and others will be left intact.

`docker stack deploy -c docker-stack.yaml`
#### Increase # of replicas

` Usage:  docker service scale SERVICE=REPLICAS [SERVICE=REPLICAS...]`

```
$ docker service scale redis=10
redis scaled to 10
overall progress: 10 out of 10 tasks
1/10: running   [==================================================>]
2/10: running   [==================================================>]
3/10: running   [==================================================>]
4/10: running   [==================================================>]
5/10: running   [==================================================>]
6/10: running   [==================================================>]
7/10: running   [==================================================>]
8/10: running   [==================================================>]
9/10: running   [==================================================>]
10/10: running   [==================================================>]
verify: Service converged
```
#### Add networks, publish ports
```
$ docker network create overlaynet --driver=overlay
v4rw68sus2al092i3pwcvc70e
[node1] (local) root@192.168.0.8 ~
$ docker service update redis --network-add overlaynet
redis
overall progress: 10 out of 10 tasks
1/10: running   [==================================================>]
2/10: running   [==================================================>]
3/10: running   [==================================================>]
4/10: running   [==================================================>]
5/10: running   [==================================================>]
6/10: running   [==================================================>]
7/10: running   [==================================================>]
8/10: running   [==================================================>]
9/10: running   [==================================================>]
10/10: running  [==================================================>]
verify: Service converged

ds2dg0m6f9mq        redis.9             redis:3.0.6         node5               Running             Running 3 minutes ago
j1dvw668bsu2         \_ redis.9         redis:3.0.6         node5               Shutdown            Shutdown 3 minutes ago
y7kgttby1vno        redis.10            redis:3.0.6         node2               Running             Running 11 seconds ago
kuw4fmiamj4m         \_ redis.10        redis:3.0.6         node2               Shutdown            Shutdown 13 seconds ago
vosm1yeq4jii         \_ redis.10        redis:3.0.6         node2               Shutdown            Shutdown 3 minutes ago
```
#### Mount volumes
`docker volume create myvol`

`docker volume ls`

`$ docker service update redis --mount-add type=volume,source=myvol,target=/var`

#### Illustrate running a replicated vs global service
```
$ docker service create --name globalserve -p 80:80 --mode global nginx:alpine
zhyknuoqjhzroj5xwcmvfwa7l
overall progress: 5 out of 5 tasks
srqv7up1ttuq: running   [==================================================>]
obfsi8vw7tja: running   [==================================================>]
x17qfaioznya: running   [==================================================>]
yxvxgz98ujxy: running   [==================================================>]
radpqalrb3o9: running   [==================================================>]
verify: Service converged

$ docker service ls
ID                  NAME                MODE                REPLICASIMAGE               PORTS
zhyknuoqjhzr        globalserve         global              5/5nginx:alpine        *:80->80/tcp
mnejoka8adty        redis               replicated          10/10redis:latest

```
#### Identify the steps needed to troubleshoot a service not deploying
`docker service inspect <svc-name>`

`docker logs`

`docker service logs redis`

#### Apply node labels to demonstrate placement of tasks
```
$ docker node update --help

Usage:  docker node update [OPTIONS] NODE

Update a node

Options:
      --availability string   Availability of the node ("active"|"pause"|"drain")
      --label-add list        Add or update a node label (key=value)
      --label-rm list         Remove a node label if exists
      --role string           Role of the node ("worker"|"manager")
```

`docker node update node1 --label-add type=ha`

```
$ docker node inspect node1 --format='{{.Spec.Labels}}'
map[master: type:ha]
```
#### Sketch how a Dockerized application communicates with legacy systems

#### Paraphrase the importance of quorum in a swarm cluster

>   Deploy odd number of managers

>   Dont deploy too many managers (More managers means more time to achieve consensus)

>   Best Practice: Spread your managers across Availability Zones within your network

#### Demonstrate the usage of templates with "docker service create"

```
$ docker service create --name hosttempl \
                        --hostname="{{.Node.Hostname}}-{{.Node.ID}}-{{.Service.Name}}"\
                         busybox top

va8ew30grofhjoychbr6iot8c

$ docker service ps va8ew30grofhjoychbr6iot8c

ID            NAME         IMAGE                                                                                   NODE          DESIRED STATE  CURRENT STATE               ERROR  PORTS
wo41w8hg8qan  hosttempl.1  busybox:latest@sha256:29f5d56d12684887bdfa50dcd29fc31eea4aaf4ad3bec43daf19026a7ce69912  2e7a8a9c4da2  Running        Running about a minute ago

$ docker inspect --format="{{.Config.Hostname}}" 2e7a8a9c4da2-wo41w8hg8qanxwjwsg4kxpprj-hosttempl

x3ti0erg11rjpg64m75kej2mz-hosttempl
```
