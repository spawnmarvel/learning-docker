FROM rabbitmq:3.12-management
COPY rabbitmq.conf /etc/rabbitmq
COPY generate-certificate.sh /tmp/generate-certificate.sh
CMD ["/tmp/generate-certificate.sh"]
RUN cat /etc/rabbitmq/rabbitmq.conf
RUN rabbitmq-plugins enable --offline rabbitmq_shovel
RUN rabbitmq-plugins enable --offline rabbitmq_shovel_management

