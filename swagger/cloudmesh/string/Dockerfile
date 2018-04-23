FROM python:2.7

MAINTAINER Rashmi Ray <rashray@iu.edu>

# Setup java 
RUN apt-get update
RUN apt-get install -q -y default-jre

# install net tools
RUN apt-get install -q -y net-tools

COPY ["Makefile", "string_init.yaml", \
      "default_controller.py",\
      "requirements.txt", "swagger-codegen-cli-2.3.1.jar", "/files/"]

WORKDIR /files
  
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

# Install the flask service using make commands
RUN make service

