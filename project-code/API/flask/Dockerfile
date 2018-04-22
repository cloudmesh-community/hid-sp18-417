FROM ubuntu:16.04

MAINTAINER Rashmi Ray <rashray@iu.edu>

RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
