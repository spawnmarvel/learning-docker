# Rmq x 2 ssl

```bash

# test the no ssl rmq x 2 compose to see that all is success
mkdir rmq-2-ssl

cp * 

docker compose up -d

```

## Rmq x 2 ssl

* test with rabbitmq.config for auth backend, internal backend
* make cert that last for 10 years
* have fun


## Certificate store CA

* openssl.cnf for config
* 
From this build (it is for windows )

https://github.com/spawnmarvel/quickguides/blob/main/securityPKI-CA/README.md

With reference to:
* https://www.rabbitmq.com/ssl.html#manual-certificate-generation
* https://pki-tutorial.readthedocs.io/en/latest/simple/root-ca.conf.html

visual

https://follow-e-lo.com/2024/01/20/docker-rabbtimq-x2-ssl/

```bash

cd rmq-x2-ssl/cert-store

openssl version
OpenSSL 3.0.2 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)

mkdir certs private
chmod 700 private # remove all permission
echo 01 > serial # should have content 01
touche index.txt

ls
certs  index.txt  openssl.cnf  private  serial

# Next we need to generate the key and certificates that our test Certificate Authority will use.

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

## Certificates for server

## Update Dockerfile

