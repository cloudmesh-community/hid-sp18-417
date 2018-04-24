FROM python:alpine

MAINTAINER Rashmi Ray <rashray@iu.edu>

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

RUN pip install flask requests && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y git-core python-pip python-dev build-essential python-flask curl
RUN pip install pandas
RUN easy_install quandl
RUN easy_install pygal

COPY app /app/

EXPOSE 5000

ENTRYPOINT ["python", "/app/main.py"]
