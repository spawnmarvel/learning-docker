# Use the official Apache HTTP Server as the base image
FROM httpd:2.4

# Copy the custom Apache configuration file to the proper location in the container
COPY httpd.conf /usr/local/apache2/conf/httpd.conf

# Copy the website files for the virtual hosts into the web root inside the container
COPY www/example /usr/local/apache2/htdocs/example

# Expose port 80 to the outside world
EXPOSE 80
