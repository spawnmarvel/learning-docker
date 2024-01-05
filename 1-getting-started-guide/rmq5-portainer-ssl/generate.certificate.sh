#!/bin/bash

# non-interactive and 10 years expiration
openssl req -x509 -newkey rsa:4096 -keyout server_key.pem -out server_cert.pem -sha256 -days 3650 -nodes \
 -subj "/C=XX/ST=NOR/L=BERG/O=CompanyName/OU=CLOUD/CN=rmq5.cloud"

# make the bundle
cp server_cert.pem server_ca.bundle

# https://stackoverflow.com/questions/44047315/generate-a-self-signed-certificate-in-docker

# https://follow-e-lo.com/2024/01/05/docker-compose-ssl/
