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


## cert store

* openssl.cnf for config
* 
From this build (it is for windows )

https://github.com/spawnmarvel/quickguides/blob/main/securityPKI-CA/README.md

With reference to:
* https://www.rabbitmq.com/ssl.html#manual-certificate-generation
* https://pki-tutorial.readthedocs.io/en/latest/simple/root-ca.conf.html

visual

https://follow-e-lo.com/2024/01/20/docker-rabbtimq-x2-ssl/