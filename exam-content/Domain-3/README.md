# Domain​ ​3:​ ​Installation​ ​and​ ​Configuration
(15%​ ​of​ ​exam) Content may include the following:
#### Demonstrate the ability to upgrade the Docker engine

https://docs.docker.com/install/linux/docker-ce/ubuntu/

#### Complete setup of repo, select a storage driver, and complete installation of Docker engine on multiple platforms

https://docs.docker.com/storage/storagedriver/select-storage-driver/

#### Configure logging drivers (splunk, journald, etc)

https://github.com/suryaval/docker-notes/blob/master/s1/s1e6.md

#### Setup swarm, configure managers, add nodes, and setup backup schedule

>   Swarm and its state is stored in /var/lib/docker/swarm

Backup:
1.  service docker stop
2.  tar -czvf /var/lib/docker/swarm
3.  service docker start
#### Create and manage user and teams

>   ORGs, TEAMs and USERs are created in UCP

```
ORG
 |_____ TEAM
          |_____ USER
```

#### Interpret errors to troubleshoot installation issues without assistance

>   Enable debugging in /etc/docker/daemon.json

```
{
  "debug": true
}
```
#### Outline the sizing requirements prior to installation
```
Minimum requirements
8GB of RAM for manager nodes or nodes running DTR
4GB of RAM for worker nodes
3GB of free disk space

Recommended production requirements
16GB of RAM for manager nodes or nodes running DTR
4 vCPUs for manager nodes or nodes running DTR
25-100GB of free disk space
```
#### Understand namespaces, cgroups, and configuration of certificates

*   Namespaces: shares OS to feel like multiple OS:

    *   ProcessID (PID)

    *   Network (net)

    *   FileSystem/Mount (mnt)

    *   Inter-Process Communication (IPC)

    *   User (user)

    *   UTS (uts)

    >   Docker container is an organized collection of namespaces

*   CGROUPS: CPU/RAM/Storage I/O

#### Use certificate-based client-server authentication to ensure a Docker daemon has the rights to access images on a registry

>   Specify the certs in /etc/docker/daemon.json

```
{
  "debug": true,
  "tls": true,
  "tlscert": "/var/docker/server.pem",
  "tlskey": "/var/docker/serverkey.pem",
  "hosts": ["tcp://192.168.59.3:2376"]
}
```

>   Configuring Registry Certs

```
/etc/docker/certs.d/        <-- Certificate directory
    └── localhost:5000          <-- Hostname:port
       ├── client.cert          <-- Client certificate
       ├── client.key           <-- Client key
       └── ca.crt               <-- Certificate authority that signed
                                    the registry certificate
```

#### Consistently repeat steps to deploy Docker engine, UCP, and DTR on AWS and on premises in an HA config

* HA config = 5 managers 0 workers or 3 managers and 2 workers

* Recommended HA for UCP/DTR will be 3 DTR nodes and 3 UCP nodes for production grade

>   Create an UCP:

`docker run --rm -dt --name ucp -v /var/run/docker.sock:/var/run/docker.sock docker/ucp:2.2.4 install --host-address <ip> --interactive`

>  Create a DTR:

`docker run --rm -dt docker/dtr install --dtr-external-url dtr.mydns.com --ucp-node dtr1 --ucp-url https://54.202.75.104 --ucp-insecure-tls`

> UCP and DTR are listed in application stacks of Universal Control Plane dashboard.

> We can add Amazon S3 as a shared storage mechanism. Join DTR replicas with this common storage.

#### Complete configuration of backups for UCP and DTR

Backing Up DTR includes the following:
*   DTR configuration
*   Repository MetaData
*   Notary Data
*   Certificates

NOTE: Images are not backed up as part of native DTR backup   

#### Configure the Docker daemon to start on boot

>   sudo systemctl enable docker
