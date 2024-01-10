FROM httpd:2.4-alpine
COPY index.html /usr/local/apache2/h2docs/
COPY my-httpd.conf /usr/local/apache2/conf/httpd.conf
WORKDIR /usr/local/apache2/htdocs/
RUN chmod 0755 /usr/local/apache2/h2docs/index.html