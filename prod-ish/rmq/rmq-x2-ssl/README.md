# Rmq x 2 ssl Certificate Authority PKI

## visual

https://follow-e-lo.com/2024/01/20/docker-rabbtimq-x2-ssl/


## Rmq x 2 ssl

* Test with rabbitmq.config for auth backend, internal backend
* Make cert that last for 10 years
* Have fun


## Certificate store CA

From this build (it is for windows )

https://github.com/spawnmarvel/quickguides/blob/main/securityPKI-CA/README.md

With reference to:
* https://www.rabbitmq.com/ssl.html#manual-certificate-generation
* https://pki-tutorial.readthedocs.io/en/latest/simple/root-ca.conf.html


The openssl.cnf for used here was translated to Linux.


```bash

cd rmq-x2-ssl
mkdir cert-store
cd cert-store
mkdir certs
ls
openssl.cnf

openssl version
OpenSSL 3.0.2 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)

mkdir certs private
chmod 700 private # remove all permission
echo 01 > serial # should have content 01
touch > index.txt
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

# view extensions, KeyUsage must be Certificate Signing, Off-line CRL Signing, CRL Signing (06) or at least keyCertSign, cRLSign
openssl x509 -noout -ext keyUsage < ca_certificate.pem
# X509v3 Key Usage:
#    Certificate Sign, CRL Sign

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

# Generating RSA private key
openssl genrsa -out ./client/private_key.pem 2048

# Generating request
openssl req -new -key ./client/private_key.pem -out ./client/req.pem -outform PEM -subj /CN=rmq_client.cloud -nodes

# Server and client extension
openssl ca -config openssl.cnf -in ./client/req.pem -out ./client/client_certificate.pem -notext -batch -extensions client_server_extension

# Using configuration from openssl.cnf
# Check that the request matches the signature
# Signature ok
# The Subject's Distinguished Name is as follows
# commonName            :ASN.1 12:'rmq_client.cloud'
# Certificate is to be certified until Jan 27 14:58:35 2034 GMT (3652 days)
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

# Generating RSA private key
openssl genrsa -out ./server/private_key.pem 2048

# Generating request
openssl req -new -key ./server/private_key.pem -out ./server/req.pem -outform PEM -subj /CN=rmq_server.cloud -nodes

# Server and client extension
openssl ca -config openssl.cnf -in ./server/req.pem -out ./server/server_certificate.pem -notext -batch  -extensions client_server_extension

# Using configuration from openssl.cnf
# Check that the request matches the signature
# Signature ok
# The Subject's Distinguished Name is as follows
# commonName            :ASN.1 12:'rmq_server.cloud'
# Certificate is to be certified until Jan 27 15:03:23 2034 GMT (3652 days)
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

bash copy_certificates.sh

```

## Test SSL

```bash

# Test ssl rmq x 2 compose to see that all is success
mkdir rmq-2-ssl

cp * 

docker compose up -d

Network rmq-x2-ssl_net_messaging                  Created                                                      
Volume "rmq-x2-ssl_vol_rabbitmq_data_rmq_client"  Created                                                     
Volume "rmq-x2-ssl_vol_rabbitmq_data_rmq_server"  Created                                                     
Container rmq_server                              Started                                                      
Container rmq_client                              Started

docker compose down

# remove volumes, remove images

# after edit
docker compose up -d --build


```

## Update server with advanced.config (and URI's)

Changed to advanced.config for server also.

Hm, this just works, that means if we use the shovel with ssl we have to use advanced.config on both.

Or I am missing something from the advanced.config translate to rabbitmq.conf (?!).

For future me to test, yes you are missing something, look below. It works.

```bash

# If needed
&versions=tlsv1.2


# does not work
# 2024-01-28 16:40:30.733577+00:00 [notice] <0.1009.0> TLS client: In state connection received SERVER ALERT: 
# Fatal - Certificate required
# 2024-01-28 16:39:30.629916+00:00 [notice] <0.766.0> TLS server: 
# In state wait_cert at tls_handshake_1_3.erl:1484 generated SERVER ALERT: Fatal - Certificate required
{uris, ["amqps://rmq_client.cloud:rmq_client.cloud-pass@rmq_server.cloud:5674"]},


# Works using user, pass and cert and no external login
# 2024-01-28 16:46:44.424664+00:00 [info] <0.769.0> connection <0.769.0> 
# (192.168.176.3:43750 -> 192.168.176.2:5674 - Shovel shovel_send1): 
# user 'rmq_client.cloud' authenticated and granted access to vhost '/'
{uris, ["amqps://rmq_client.cloud:rmq_client.cloud-pass@rmq_server.cloud:5674?
cacertfile=/etc/rabbitmq/ca.bundle&
certfile=/etc/rabbitmq/client_certificate.pem&
keyfile=/etc/rabbitmq/private_key.pem&
verify=verify_peer&
fail_if_no_peer_cert=true&
server_name_indication=rmq_server.cloud&
heartbeat=15"]},

# works since it uses the CN from the client_certificate.pem and external login from CN
# connect to server-name, with SSL and EXTERNAL authentication
# 2024-01-28 16:49:29.838741+00:00 [info] <0.769.0> connection <0.769.0> 
# (192.168.192.3:39936 -> 192.168.192.2:5674 - Shovel shovel_send1): 
# user 'rmq_client.cloud' authenticated and granted access to vhost '/'
{uris, ["amqps://@rmq_server.cloud:5674?
cacertfile=/etc/rabbitmq/ca.bundle&
certfile=/etc/rabbitmq/client_certificate.pem&
keyfile=/etc/rabbitmq/private_key.pem&
verify=verify_peer&
fail_if_no_peer_cert=true&
server_name_indication=rmq_server.cloud
&auth_mechanism=external&
heartbeat=15"]},

# works also, since it uses the CN from the client_certificate.pem and external login from 
# CN and bypass or username in that case.
# connect to server-name, with SSL and EXTERNAL authentication
{uris, ["amqps://rmq_client.cloud@rmq_server.cloud:5674?
cacertfile=/etc/rabbitmq/ca.bundle&
certfile=/etc/rabbitmq/client_certificate.pem&
keyfile=/etc/rabbitmq/private_key.pem&
verify=verify_peer&
fail_if_no_peer_cert=true&
server_name_indication=rmq_server.cloud&
auth_mechanism=external&
heartbeat=15"]},
```


## Update server with advanced.config to rabbitmq.conf translation success

This must be possible, update on server

```bash
rmq-x2-ssl/server

cp advanced.config advanced.config_
sudo nano advanced.config_
# [].
cp advanced.config advanced.config_bck
cp advanced.config_ advanced.config
cp rabbitmq.conf rabbitmq.conf_bck

```

Edit rabbitmq.conf

```bash

[...]

ssl_options.verify     = verify_peer
ssl_options.fail_if_no_peer_cert = true

ssl_options.depth  = 2

auth_mechanisms.1 = PLAIN
auth_mechanisms.1 = AMQPLAIN
auth_mechanisms.1 = EXTERNAL

ssl_cert_login_from = common_name

auth_backends.1   = rabbit_auth_backend_internal


```

success

```log
2024-01-28 20:22:59.664880+00:00 [info] <0.769.0> connection <0.769.0> (172.26.0.3:51818 -> 172.26.0.2:5674) has a client-provided name: Shovel shovel_send3

2024-01-28 20:22:59.666713+00:00 [info] <0.769.0> connection <0.769.0> (172.26.0.3:51818 -> 172.26.0.2:5674 - Shovel shovel_send3): user 'rmq_client.cloud' authenticated and granted access to vhost '/'
```

The error was from:

* ssl_options.verify     = verify_none / set peer
* ssl_options.fail_if_no_peer_cert = false / set true

```log
2024-01-28 19:54:26.579934+00:00 [error] <0.852.0> Error on AMQP connection <0.852.0> (172.21.0.3:34270 -> 172.21.0.2:5674, state: starting):
2024-01-28 19:54:26.579934+00:00 [error] <0.852.0> EXTERNAL login refused: connection peer presented no TLS (x.509) certificate
```

x509 (TLS/SSL) certificate Authentication Mechanism for RabbitMQ

https://github.com/rabbitmq/rabbitmq-server/tree/main/deps/rabbitmq_auth_mechanism_ssl

## 2024-01-28 11:04:34.720799+00:00 [error] <0.897.0> EXTERNAL login refused using only rabbitmq.conf for server

Continue here with this error

```log

This should work out of the box:

{uris, ["amqps://rmq_client.cloud@rmq_server.cloud:5674?cacertfile=/etc/rabbitmq/ca.bundle&certfile=/etc/rabbitmq/client_certificate.pem&keyfile=/etc/rabbitmq/private_key.pem&verify=verify_peer&fail_if_no_peer_cert=true&server_name_indication=rmq_server.cloud&auth_mechanism=external&heartbeat=15"]},

2024-01-28 11:04:34.720799+00:00 [error] <0.897.0> EXTERNAL login refused: connection peer presented no TLS (x.509) certificate

Same error with append tlsv1.2:

{uris, ["amqps://rmq_client.cloud@rmq_server.cloud:5674?cacertfile=/etc/rabbitmq/ca.bundle&certfile=/etc/rabbitmq/client_certificate.pem&keyfile=/etc/rabbitmq/private_key.pem&verify=verify_peer&fail_if_no_peer_cert=true&server_name_indication=rmq_server.cloud&auth_mechanism=external&versions=tlsv1.2&heartbeat=15"]},

Make error in shovel, wrong file, cacertfile=/etc/rabbitmq/caca.bundle:

2024-01-28 12:50:56.825375+00:00 [error] <0.859.0> Shovel 'shovel_put' failed to connect (URI: amqps://rmq_server.cloud:5674): {options,{cacertfile,"/etc/rabbitmq/caca.bundle",{error,enoent}}}

is correct behaviour, the file caca.bundle does not exists.

Step back and test URI amqps:

{uris, ["amqps://rmq_client.cloud:rmq_client.cloud-pass@rmq_server.cloud:5674"]},

rmq_server  | 2024-01-28 15:10:53.524846+00:00 [info] <0.769.0> connection <0.769.0> (192.168.16.3:39366 -> 192.168.16.2:5674 - Shovel shovel_put): user 'rmq_client.cloud' authenticated and granted access to vhost '/'

Good, this works, wtf is up with the cert for the shovel?

Added advanced.config to server and success, hm..


```

## (FIXED) X509 Error 32 - Key usage does not include certificate signing	The certificate of the CA currently being examined in the signing chain was rejected because its Key Usage: extension does not permit certificate signing.


{uris, ["amqps://rmq_client.cloud@rmq_server.cloud:5674?cacertfile=/etc/rabbitmq/ca.bundle&certfile=/etc/rabbitmq/client_certificate.pem&keyfile=/etc/rabbitmq/private_key.pem&verify=verify_peer&fail_if_no_peer_cert=true&server_name_indication=rmq_server.cloud&auth_mechanism=external&heartbeat=15"]},

```bash
# 2024-01-28 11:04:34.720799+00:00 [error] <0.897.0> EXTERNAL login refused: connection peer presented no TLS (x.509) certificate

# ran 
cd /etc/rabbitmq
cp ca.bundle ca_certificate.pem
openssl s_server -accept 8443 -cert server_certificate.pem -key private_key.pem -CAfile ca_certificate.pem -tls1_2
#

cd /etc/rabbitmq
cp ca.bundle ca_certificate.pem
openssl s_client -connect rmq_server.cloud:8443 -cert client_certificate.pem -key private_key.pem -CAfile ca_certificate.pem -tls1_2
# Secure Renegotiation IS supported

```

```log

depth=1 CN = SocratesIncCa
verify error:num=79:invalid CA certificate
verify return:1
depth=1 CN = SocratesIncCa
verify error:num=26:unsuitable certificate purpose
verify return:1
depth=1 CN = SocratesIncCa
verify return:1
depth=1 CN = SocratesIncCa
verify error:num=32:key usage does not include certificate signing
verify return:1
depth=0 CN = rmq_server.cloud
verify return:1
[...]
No client certificate CA names sent
[..]
Verify return code: 32 (key usage does not include certificate signing)

```
SSL/TLS error messages

* X509 Error 32 - Key usage does not include certificate signing	The certificate of the CA currently being examined in the signing chain was rejected because its Key Usage: extension does not permit certificate signing.

https://help.fortinet.com/fweb/551/log/Content/FortiWeb/fortiweb-log/SSL_TLS_error_messages.htm


```bash
# fixed using openssl.cfg
# view extensions, KeyUsage must be Certificate Signing, Off-line CRL Signing, CRL Signing (06) or at least keyCertSign, cRLSign
openssl x509 -noout -ext keyUsage < ca_certificate.pem
# X509v3 Key Usage:
#    Certificate Sign, CRL Sign

```


## Notes on start (just one time)

Seems like there could be one error related to docker, just one time.

```log
2024-01-16 21:37:11.386120+00:00 [error] <0.826.0>                          {header,<<"authorization">>},
2024-01-16 21:37:11.386120+00:00 [error] <0.826.0>                          'Malformed header. Please consult the relevant specification.'},

```

https://github.com/docker-library/rabbitmq/issues/433

You are right. It is really the permission problem caused by the setting of the hostname property.