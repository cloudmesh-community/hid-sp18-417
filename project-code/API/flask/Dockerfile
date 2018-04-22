FROM ubuntu:16.04

MAINTAINER Rashmi Ray <rashray@iu.edu>

RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /flask
RUN pip install -r requirements.txt
RUN easy_install quandl
ENTRYPOINT ["python"]
CMD ["app.py"]
