#!/bin/bash
# make the bundle
# pwd
# rmq-x2-ssl/
cp cert-store/ca_certificate.pem ./client/ca.bundle
cp cert-store/ca_certificate.pem ./server/ca.bundle

# copy client cert and key
cp cert-store/client/client_certificate.pem ./client/client_certificate.pem
cp cert-store/client/private_key.pem ./client/private_key.pem

# copy server cert and key
cp cert-store/server/server_certificate.pem ./server/server_certificate.pem
cp cert-store/server/private_key.pem ./server/private_key.pem