# Rmq x 2 ssl Certificate Authority PKI

## visual

https://follow-e-lo.com/2024/01/20/docker-rabbtimq-x2-ssl/


## Rmq x 2 ssl

* test with rabbitmq.config for auth backend, internal backend
* make cert that last for 10 years
* have fun


## Certificate store CA

From this build (it is for windows )

https://github.com/spawnmarvel/quickguides/blob/main/securityPKI-CA/README.md

With reference to:
* https://www.rabbitmq.com/ssl.html#manual-certificate-generation
* https://pki-tutorial.readthedocs.io/en/latest/simple/root-ca.conf.html


The openssl.cnf for used here was translated to Linux.


```bash

cd rmq-x2-ssl/cert-store

openssl version
OpenSSL 3.0.2 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)

mkdir certs private
chmod 700 private # remove all permission
echo 01 > serial # should have content 01
touch index.txt

ls
certs  index.txt  openssl.cnf  private  serial

# Next we need to generate the key and certificates that our test Certificate Authority will use. Since we are uing a custom openssl.cnf we have already added where the key should be stored.
# You could generate your own key with a password protection
# https://www.ibm.com/docs/en/license-metric-tool?topic=certificate-step-1-creating-private-keys-certificates

# 1 Generate the key and cert
/rmq-x2-ssl/cert-store

openssl req -x509 -config openssl.cnf -newkey rsa:2048 -days 3652 -out ca_certificate.pem -outform PEM -subj /CN=SocratesIncCa/ -nodes


/rmq-x2-ssl/cert-store/private ls
ca_private_key.pem

/rmq-x2-ssl/cert-store ls
ca_certificate.pem  certs  index.txt  openssl.cnf  private  serial

# Generate certificate DER form
openssl x509 -in ca_certificate.pem  -out ca_certificate.cer -outform DER

/rmq-x2-ssl/cert-store ls
ca_certificate.cer  ca_certificate.pem  certs  index.txt  openssl.cnf  private  serial

# view the CN
openssl x509 -noout -subject -in ca_certificate.pem

subject=CN = SocratesIncCa

# This is all that is needed to generate a test Certificate Authority. The root certificate is in ca_certificate.pem and is also in ca_certificate.cer. 
# These two files contain the same information, but in different formats, PEM and DER. 
# Most software uses the former but some tools require the latter.
```

In the compose we have two services for rmq with name

*  hostname: rmq_client.cloud
*  hostname: rmq_server.cloud

We need to generate CN with that name and also add rmq_client.cloud as a user on rmq_server.cloud.

Since we will be using CN for login.

## Certificates for server (client) rmq_client.cloud

rmq_client.cloud

```bash
cd cert-store
mkdir client

cd

# Generating RSA private key
openssl genrsa -out ./client/private_key.pem 2048

# Generating request
openssl req -new -key ./client/private_key.pem -out ./client/req.pem -outform PEM -subj /CN=rmq_client.cloud -nodes

# Server and client extension
openssl ca -config openssl.cnf -in ./client/req.pem -out ./client/client_certificate.pem -notext -batch -extensions usr_cert

# Using configuration from openssl.cnf
# Check that the request matches the signature
# Signature ok
# The Subject's Distinguished Name is as follows
# commonName            :ASN.1 12:'rmq_client.cloud'
# Certificate is to be certified until Jan 20 12:50:28 2034 GMT (3652 days)
# Write out database with 1 new entries
# Data Base Updated


# view cn
openssl x509 -noout -subject -in ./client/client_certificate.pem

subject=CN = rmq_client.cloud

# view extensions
openssl x509 -noout -ext keyUsage < ./client/client_certificate.pem
# X509v3 Key Usage:
#    Digital Signature, Non Repudiation, Key Encipherment

openssl x509 -noout -ext extendedKeyUsage < ./client/client_certificate.pem
# X509v3 Extended Key Usage:
#    TLS Web Server Authentication, TLS Web Client Authentication, Code Signing, E-mail Protection

# cp to windows import in certificate
cat ./client/client_certificate.pem
# import in windows as client_certificate.crt
# Intended purposes = all

# all files
/rmq-x2-ssl/cert-store ls
ca_certificate.cer  certs   index.txt       index.txt.old  private  serial.old
ca_certificate.pem  client  index.txt.attr  openssl.cnf    serial

# server (client)
cd client
ls
client_certificate.pem  private_key.pem  req.pem
cd ..
cd certs
ls
01.pem

```

## Certificates for server (server) rmq_server.cloud

rmq_server.cloud

```bash
cd cert-store
mkdir server

cd

# Generating RSA private key
openssl genrsa -out ./server/private_key.pem 2048

# Generating request
openssl req -new -key ./server/private_key.pem -out ./server/req.pem -outform PEM -subj /CN=rmq_server.cloud -nodes

# Server and client extension
openssl ca -config openssl.cnf -in ./server/req.pem -out ./server/server_certificate.pem -notext -batch -extensions usr_cert

# Using configuration from openssl.cnf
# Check that the request matches the signature
# Signature ok
# The Subject's Distinguished Name is as follows
# commonName            :ASN.1 12:'rmq_server.cloud'
# Certificate is to be certified until Jan 26 11:05:01 2034 GMT (3652 days)
# Write out database with 1 new entries
# Data Base Updated

# view cn
openssl x509 -noout -subject -in ./server/server_certificate.pem

subject=CN = rmq_server.cloud

# view extensions
openssl x509 -noout -ext keyUsage < ./server/server_certificate.pem
# X509v3 Key Usage:
#    Digital Signature, Non Repudiation, Key Encipherment

openssl x509 -noout -ext extendedKeyUsage < ./server/server_certificate.pem
# X509v3 Extended Key Usage:
#    TLS Web Server Authentication, TLS Web Client Authentication, Code Signing, E-mail Protection

# server (server)
cd client
ls
private_key.pem  req.pem  server_certificate.pem
cd ..
cd certs
ls
01.pem  02.pem
```
## Make bundle and copy all certificates

```bash
# make the bundle
pwd
rmq-x2-ssl/

cp cert-store/ca_certificate.pem ./client/ca.bundle
cp cert-store/ca_certificate.pem ./server/ca.bundle

# copy client cert and key
cp cert-store/client/client_certificate.pem ./client/client_certificate.pem
cp cert-store/client/private_key.pem ./client/private_key.pem

# copy server cert and key
cp cert-store/server/server_certificate.pem ./server/server_certificate.pem
cp cert-store/server/private_key.pem ./server/private_key.pem

```
## Test no SSL

```bash

# test the no ssl rmq x 2 compose to see that all is success
mkdir rmq-2-ssl

cp * 

docker compose up -d

Network rmq-x2-ssl_net_messaging                  Created                                                      
Volume "rmq-x2-ssl_vol_rabbitmq_data_rmq_client"  Created                                                     
Volume "rmq-x2-ssl_vol_rabbitmq_data_rmq_server"  Created                                                     
Container rmq_server                              Started                                                      
Container rmq_client                              Started

docker compose down

# after edit
docker compose up -d --build


```

## Update Dockerfile and configuration

* add CN user to definitions for both
* update Dockerfile to cp certificates
* update shovel


rmq_client.cloud

definitions

```json
 }, {
      "name": "rmq_server.cloud",
      "password": "rmq_server.cloud-pass",
      "tags": "administrator"
    }],
```

```bash
# Dockerfile_client
COPY /client/ca.bundle /etc/rabbitmq
COPY /client/client_certificate.pem /etc/rabbitmq
COPY /client/private_key.pem /etc/rabbitmq
RUN chmod 664 /etc/rabbitmq/ca.bundle
RUN chmod 664 /etc/rabbitmq/client_certificate.pem
RUN chmod 664 /etc/rabbitmq/private_key.pem

```

rmq_server.cloud

definitions

```json
 }, {
      "name": "rmq_server.cloud",
      "password": "rmq_server.cloud-pass",
      "tags": "administrator"
    }],
```

```bash
# Dockerfile_server
COPY /server/ca.bundle /etc/rabbitmq
COPY /server/server_certificate.pem /etc/rabbitmq
COPY /server/private_key.pem /etc/rabbitmq
RUN chmod 664 /etc/rabbitmq/ca.bundle
RUN chmod 664 /etc/rabbitmq/server_certificate.pem
RUN chmod 664 /etc/rabbitmq/private_key.pem

```

advanced.config

```bash

 {uris, ["amqp://rmq_server.cloud:rmq_server.cloud-pass@rmq_server.cloud:5673"]},

```
Lets make sure it starts and all files are copied

```bash
docker compose up -d --build
#success

# enter rmq_server
/etc/rabbitmq
ls
ca.bundle  conf.d  definitions.json  enabled_plugins  private_key.pem  rabbitmq.conf  server_certificate.pem

# enter rmq_client
/etc/rabbitmq
ls
advanced.config  ca.bundle  client_certificate.pem  conf.d  definitions.json  enabled_plugins  private_key.pem  rabbitmq.conf
```

## Configure SSL

* configure ssl in rabbitmq.conf for both
* update advanced config to use an SSL port

rmq_client.cloud

rabbitmq.conf
* update to ssl section
* update ports in compose

```bash
docker compose down
# move files
docker compose up -d --build

2024-01-27 12:49:36.908157+00:00 [info] <0.568.0> Management plugin: HTTPS listener started on port 15671
# [..]
2024-01-27 12:49:36.919293+00:00 [info] <0.680.0> started TCP listener on [::]:5672

2024-01-27 12:49:36.921088+00:00 [info] <0.712.0> started TLS (SSL) listener on [::]:5671

 completed with 6 plugins.
```


rmq_client.server

rabbitmq.conf
* TBD

## Notes on start

Seems like there could be one error related to docker, just one time.

```log
2024-01-16 21:37:11.386120+00:00 [error] <0.826.0>                          {header,<<"authorization">>},
2024-01-16 21:37:11.386120+00:00 [error] <0.826.0>                          'Malformed header. Please consult the relevant specification.'},

```

https://github.com/docker-library/rabbitmq/issues/433

You are right. It is really the permission problem caused by the setting of the hostname property.