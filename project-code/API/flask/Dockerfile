FROM ubuntu:16.04

MAINTAINER Rashmi Ray <rashray@iu.edu>

RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y git-core python-pip python-dev build-essential python-flask curl
RUN pip install pandas
RUN easy_install quandl
RUN easy_install pygal
RUN git clone https://github.com/cloudmesh-community/hid-sp18-417.git
WORKDIR /hid-sp18-417/project-code/API/flask
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
