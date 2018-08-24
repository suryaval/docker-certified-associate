# Domain​ ​4:​ ​Networking​ ​
(15%​ ​of​ ​exam) Content may include the following:
#### Create a Docker bridge network for a developer to use for their containers
`ubuntu@ip-172-31-26-145:~$ docker network create developer-network -d bridge`

```
fb23f1b5bdc2ea3d9dc5bc1a57faff29070bb14fc5612653aea8c9ee6f095571
ubuntu@ip-172-31-26-145:~$ docker network ls | grep developer-network
fb23f1b5bdc2        developer-network   bridge              local
ubuntu@ip-172-31-26-145:~$ docker network inspect developer-network
[
    {
        "Name": "developer-network",
        "Id": "fb23f1b5bdc2ea3d9dc5bc1a57faff29070bb14fc5612653aea8c9ee6f095571",
        "Created": "2018-08-18T18:50:07.991112794Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.19.0.0/16",
                    "Gateway": "172.19.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
```
#### Troubleshoot container and engine logs to understand a connectivity issue between containers

`docker logs <container-id>`

#### Publish a port so that an application is accessible externally

`docker run -dit nginx:latest -p 80:80 --name web-server --network developer-network`

#### Identify which IP and port a container is externally accessible on
```
$ docker port 0b34bf293d39
80/tcp -> 0.0.0.0:80
```
#### Describe the different types and use cases for the built-in network drivers
```
bridge

host

overlay
```
#### Understand the Container Network Model and how it interfaces with the Docker engine and network and IPAM drivers
* sandbox
* endpoint
* network
* Network Controller
* Driver

#### Configure Docker to use external DNS

In /etc/docker/daemon.json

```
{
    "dns": ["10.0.0.2", "8.8.8.8"]
}

```
#### Use Docker to load balance HTTP/HTTPs traffic to an application (Configure L7 load balancing with Docker EE)

#### Understand and describe the types of traffic that flow between the Docker engine, registry, and UCP controllers

#### Deploy a service on a Docker overlay network
```
ubuntu@ip-172-31-26-145:~$ docker network create --driver=overlay --subnet=172.19.0.0/24 overlay0
cun9u3fzvyna249t275s1vq6d
ubuntu@ip-172-31-26-145:~$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
b6abb703fdb8        bridge              bridge              local
fb23f1b5bdc2        developer-network   bridge              local
06817a5e8a4a        docker_gwbridge     bridge              local
i9jcecb2s5rx        dtr-ol              overlay             swarm
0056c79bddd6        host                host                local
ekg72q2ncvop        ingress             overlay             swarm
36d00ac0ebb7        none                null                local
cun9u3fzvyna        overlay0            overlay             swarm
ubuntu@ip-172-31-26-145:~$ docker network inspect overlay0
[
    {
        "Name": "overlay0",
        "Id": "cun9u3fzvyna249t275s1vq6d",
        "Created": "2018-08-23T22:49:39.346265236Z",
        "Scope": "swarm",
        "Driver": "overlay",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.19.0.0/24",
                    "Gateway": "172.19.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": null,
        "Options": {
            "com.docker.network.driver.overlay.vxlanid_list": "4098"
        },
        "Labels": null
    }
]
```
>   when a service is deployed on a overlay network, worker nodes also will get the network. FOllowing excerpt shows that overlay0 is available on worker node even though it is created on a master node. Since it is a swarm scoped network
```
ubuntu@ip-172-31-19-240:~$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
beaa33ab0b81        bridge              bridge              local
a6b219d1e025        docker_gwbridge     bridge              local
i9jcecb2s5rx        dtr-ol              overlay             swarm
6b39102a6f6a        host                host                local
ekg72q2ncvop        ingress             overlay             swarm
8ff5e8691eca        none                null                local
cun9u3fzvyna        overlay0            overlay             swarm
```
#### Describe the difference between "host" and "ingress" port publishing mode
```
In host network's port publishing mode, you are responsible for knowing where all instances are at all times, controlled with 'mode=host' in deployment

In ingress port publishing mode, it makes all published ports available on all hosts(nodes & workers)
```
* Network Driver Types:
    *   Bridge
    *   None
    *   Host
    *   Overlay
    *   Ingress
    *   Docker Gateway Bridge
    
* Bridge Network:
    *   default networkon stand-alone Docker hosts
    *   all containers on a host using bridge network can communicate
    
* None Network:
    *  Containers using this network will not get networking access at all
    
* Host Network:
    *   access container ports only from host system
    
* Overlay Network:
    *   Swarm scoped network
    *   Network will be available in the swarm enabled hosts
    
* Ingress Network:
    * network that load balances traffic between working nodes
    * maintains list of node-ips that are running a service and when request(to access a service) comes in, routes to one of them
    * provides routing mesh that allows services to be exposed externally
    
* Docker Gateway Bridge:
    * special bridge network that allows other networks access a docker daemon's physical network
