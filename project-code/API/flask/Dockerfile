FROM python:2.7

MAINTAINER Rashmi Ray <rashray@iu.edu>

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
##RUN apt-get update
##RUN apt-get update -y
##RUN apt-get install -y pytho
##RUN pip install flask requests && \
  ##  apk add --no-cache curl && \
    ##rm -rf /var/cache/apk/*

RUN apt-get update
RUN apt-get update -y
##FROM ubuntu:latest
##MAINTAINER Rajdeep Dua "dua_rajdeep@yahoo.com"
##RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
##RUN apk add git-core python-pip python-dev build-essential python-flask curl
RUN pip install pandas
RUN easy_install quandl
RUN easy_install pygal
RUN easy_install-2.7 DateTime

##COPY app /app/

EXPOSE 5000

ENTRYPOINT ["python", "/app/app/main.py"]
