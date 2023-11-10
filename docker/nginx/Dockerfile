FROM nginx:1.25.3

RUN echo 'alias ll="ls -la"' >> ~/.bashrc
RUN apt-get update
RUN apt-get install -y nano less

COPY ./htdocs /var/www/pysock
WORKDIR /var/www/pysock
