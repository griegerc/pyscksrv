FROM nginx:1.23.2-alpine

RUN echo 'alias ll="ls -la"' >> ~/.bashrc
RUN apk update
RUN apk add nano less nano

COPY ./htdocs /var/www/pysock
WORKDIR /var/www/pysock
