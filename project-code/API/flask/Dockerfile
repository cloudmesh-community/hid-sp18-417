FROM ubuntu:16.04

MAINTAINER Rashmi Ray <rashray@iu.edu>

RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y git-core python-pip python-dev build-essential python-flask
WORKDIR /flask
RUN easy_install quandl
ENTRYPOINT ["python"]
CMD ["app.py"]
