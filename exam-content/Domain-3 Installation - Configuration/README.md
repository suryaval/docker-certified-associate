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

```
INFO[0000] Beginning Docker Trusted Registry installation
ucp-password:
INFO[0004] Validating UCP cert
INFO[0004] Connecting to UCP
INFO[0005] health checking ucp
INFO[0005] Only one available UCP node detected. Picking UCP node 'ip-172-31-19-240'
INFO[0005] Searching containers in UCP for DTR replicas
INFO[0005] Searching containers in UCP for DTR replicas
INFO[0005] verifying [80 443] ports on ip-172-31-19-240
INFO[0010] Waiting for running dtr-phase2 container to finish
INFO[0010] starting phase 2
INFO[0000] Validating UCP cert
INFO[0000] Connecting to UCP
INFO[0000] health checking ucp
INFO[0000] Verifying your system is compatible with DTR
INFO[0000] Checking if the node is okay to install on
INFO[0000] Creating network: dtr-ol
INFO[0000] Connecting to network: dtr-ol
INFO[0000] Waiting for phase2 container to be known to the Docker daemon
INFO[0001] Setting up replica volumes...
INFO[0001] Creating initial CA certificates
INFO[0001] Bootstrapping rethink...
INFO[0001] Creating dtr-rethinkdb-5fc87377909f...
INFO[0009] Establishing connection with Rethinkdb
INFO[0010] Waiting for database dtr2 to exist
INFO[0010] Establishing connection with Rethinkdb
INFO[0010] Generated TLS certificate.                    dnsNames=[*.com *.*.com example.com *.dtr *.*.dtr] domains=[*.com *.*.com 172.17.0.1 example.com *.dtr *.*.dtr] ipAddresses=[172.17.0.1]
INFO[0011] License config copied from UCP.
INFO[0011] Migrating db...
INFO[0000] Establishing connection with Rethinkdb
INFO[0000] Migrating database schema                     fromVersion=0 toVersion=9
INFO[0006] Waiting for database notaryserver to exist
INFO[0007] Waiting for database notarysigner to exist
INFO[0007] Waiting for database jobrunner to exist
INFO[0009] Migrated database from version 0 to 9
INFO[0020] Starting all containers...
INFO[0020] Getting container configuration and starting containers...
INFO[0021] Recreating dtr-rethinkdb-5fc87377909f...
INFO[0025] Creating dtr-registry-5fc87377909f...
INFO[0030] Creating dtr-garant-5fc87377909f...
INFO[0035] Creating dtr-api-5fc87377909f...
INFO[0049] Creating dtr-notary-server-5fc87377909f...
INFO[0055] Recreating dtr-nginx-5fc87377909f...
INFO[0060] Creating dtr-jobrunner-5fc87377909f...
INFO[0078] Creating dtr-notary-signer-5fc87377909f...
INFO[0083] Creating dtr-scanningstore-5fc87377909f...
INFO[0088] Trying to get the kv store connection back after reconfigure
INFO[0088] Establishing connection with Rethinkdb
INFO[0089] Verifying auth settings...
INFO[0089] Successfully registered dtr with UCP
INFO[0089] Establishing connection with Rethinkdb
INFO[0089] Background tag migration started
INFO[0089] Installation is complete
INFO[0089] Replica ID is set to: 5fc87377909f
INFO[0089] You can use flag '--existing-replica-id 5fc87377909f' when joining other replicas to your Docker Trusted Registry Cluster
```
#### Configure the Docker daemon to start on boot

>   sudo systemctl enable docker
