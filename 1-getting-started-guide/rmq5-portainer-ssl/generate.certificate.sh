#!/bin/bash

openssl genrsa -des3 -passout pass:x -out server.pass.key 2048
openssl rsa -passin pass:x -in server.pass.key -out server.key
rm server.pass.key
openssl req -new -key server.key -out server.csr \
    -subj "/C=UK/ST=RMQ/L=Learn/O=OrgName/OU=IT Department/CN=rmq5.cloud"
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

# https://stackoverflow.com/questions/44047315/generate-a-self-signed-certificate-in-docker

# https://follow-e-lo.com/2024/01/05/docker-compose-ssl/
