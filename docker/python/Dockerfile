FROM python:3.9.18

RUN echo 'alias ll="ls -la"' >> ~/.bashrc
RUN apt-get update
RUN apt-get install -y nano less

RUN pip3 install websockets

COPY ./server /pysock
WORKDIR /pysock

EXPOSE 8765
CMD ["python3", "srv.py"]
#ENTRYPOINT tail -f /dev/null