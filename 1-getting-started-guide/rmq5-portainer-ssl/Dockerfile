FROM rabbitmq:3.12-management
COPY rabbitmq.conf /etc/rabbitmq
# COPY generate-certificate.sh /tmp/generate-certificate.sh
# CMD ["/tmp/generate-certificate.sh"]
COPY server_cert.pem /etc/rabbitmq
COPY server_key.pem /etc/rabbitmq
COPY server_ca.bundle /etc/rabbitmq
RUN chmod 664 /etc/rabbitmq/server_ca.bundle
RUN chmod 664 /etc/rabbitmq/server_cert.pem
RUN chmod 664 /etc/rabbitmq/server_key.pem
RUN cat /etc/rabbitmq/rabbitmq.conf
RUN rabbitmq-plugins enable --offline rabbitmq_shovel
RUN rabbitmq-plugins enable --offline rabbitmq_shovel_management

