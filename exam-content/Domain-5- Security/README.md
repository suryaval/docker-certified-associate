# Domain​ ​5:​ ​Security​ ​
(15%​ ​of​ ​exam) Content may include the following:
Describe the process of signing an image

#### Demonstrate that an image passes a security scan

* Enable security scans on a private repo
* Push to the private repo from workspace
* Image will be scanned and vulnerabilities will be reported
* Enable On-Push/Manual image scanning in Docker Trusted Registry (DTR)

#### Enable Docker Content Trust
```
Sign and push an image
Enable Docker content trust, and push your image to the registry:

$ export DOCKER_CONTENT_TRUST=1
$ docker push {dtr_url/registry_url}/{account}/{repository}:{tag}
```
#### Configure RBAC in UCP

1. Create Role: Details+Operations
2. Create Grant: Select Role + Subjects(Organization or Teams)+Collection

#### Integrate UCP with LDAP/AD
```
Login to UCP.

Navigate to admin -> admin-settings -> Authentication & Authorization

Select LDAP-Enabled: Yes

Add LDAP configuration details
```

#### Demonstrate creation of UCP client bundles

`Download the client bundles from my-profile -> client bundles
store the location of certs to an environment variable so that docker daemon will identify it.
Based on the role for the user, the docker daemon will assume the capabilities for the user using client bundles`
Client bundles contain the following:
* Account Security Key
* Environment variables
* UCP certificate files

#### Describe default engine security

`
Namespaces:
CGroups:
limited attack surface for docker daemon
`
#### Describe swarm default security
```
SWARM Security: Mutual TLS
certificate rotation
worker and manager crt exchange
```

#### Describe MTLS
```
In swarm self signed certificates will be generated and maintained among all nodes in swarm
manager communicates with other managers and nodes via Mutual TLS
TLS(Transport Layer Security) tokens are exchanged between various nodes across swarm
```

#### Identity roles
```
NONE:
VIEW ONLY:
RESTRICTED CONTROL:
SCHEDULER:
FULL CONTROL:
```

#### Describe the difference between UCP workers and managers

Managers are created using the RAFT Consensus Algorithm

#### Describe process to use external certificates with UCP and DTR

`Login into UCP -> Admin Settings -> Certificates and add all external certificates`
