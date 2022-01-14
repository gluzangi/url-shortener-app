FROM python:3.10

# set environment variable
#
ARG VERSION="python-fastapi-dev"
ARG DEBIAN_FRONTEND="noninteractive"

# set maintenance info
#
LABEL maintainer="gerald.luzangi@gmail.com"
LABEL release-date="2022-01-11"
LABEL version.is-production="$VERSION"

RUN set -x \
    && apt-get update -y && apt-get upgrade -y && apt-get install -y apt-utils autoconf automake build-essential \
    coreutils apt-transport-https aria2 ca-certificates curl git gnupg less \
    libssl-dev libcurl4-openssl-dev libpq-dev libtool libxml2-dev libxslt-dev python3-dev python3-pip vim \
    && apt-get autoremove \
    && apt-get clean

# set app-infra library and extra packages requirements
#
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# set fastapi
#
RUN pip3 install -U pip fastapi uvicorn

# set web application libs
#
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app-code /code/app

EXPOSE 8081

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
