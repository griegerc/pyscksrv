# pyscksrv

## Summary

This is a proof of concept project and playground for creating and 
running a Server/Client combination communicating with Websockets.

    Backend: Python
    Frontend: Javascript

## Setup

You need a host entry for **pysock.local**. For Windows users its adding the 
following line to the file *C:\Windows\System32\drivers\etc\hosts*:

    127.0.0.1 pysock.local
    
For a local setup with Docker you just have to build and start the 
containers in the main folder with:

    docker-compose up -d
    
After the images are built and the containers are started, you should be 
able to see the page in the browser when calling the URL:

    http://pysock.local/index.html
 