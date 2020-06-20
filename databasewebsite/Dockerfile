FROM ubuntu:18.04
LABEL Name=datadisplay Version=0.0.1
ADD . /usr/src/datadisplay
WORKDIR /usr/src/datadisplay

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get install nodejs npm -y && apt-get install postgresql postgresql-contrib -y
RUN update-rc.d postgresql enable
RUN service postgresql start
RUN npm install
#CMD ["npm","test"]