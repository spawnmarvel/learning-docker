FROM rabbitmq:3.12-management
COPY rabbitmq.conf /etc/rabbitmq
RUN cat /etc/rabbitmq/rabbitmq.conf
RUN rabbitmq-plugins enable --offline rabbitmq_shovel && rabbitmq-plugins enable --offline rabbitmq_shovel_management
