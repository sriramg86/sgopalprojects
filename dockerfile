FROM ubuntu:16.04

RUN apt-get update

RUN apt-get install -y python3.5 python3-pip

RUN pip3 install flask

RUN pip3 install flask_restful

COPY tflstatusAPI.py /opt/tflstatusAPI.py

ENTRYPOINT python3 /opt/tflstatusAPI.py
