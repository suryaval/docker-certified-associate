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

#### Describe the difference between "host" and "ingress" port publishing mode

