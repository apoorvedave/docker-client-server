#!/bin/bash

#Demo Script:

# docker create bridge network
echo "Creating a docker network: catnetwork..."
docker network create -d bridge catnetwork

# docker build data vol image
# docker build server image
# docker build client image
echo "Creating image files for data vol (imdata), server(imserver) and client(imclient)..."
docker build -f DockerfileData -t imdata .
docker build -f DockerfileServer -t imserver .
docker build -f DockerfileClient -t imclient .

# docker run data vol image
# docckr run catserver , networked, with volumes, daemon
# docker run catclient , networked, with volumes, daemon
echo "Running server and client..."
docker create --name catdata imdata
docker run -d --net=catnetwork --volumes-from catdata --name catserver imserver python /src/server.py /data/string.txt 9000
docker run -d --net=catnetwork --volumes-from catdata --name catclient imclient python /src/client.py /data/string.txt 9000

#logs
echo "###########################################"
echo "Display client logs..."
echo "###########################################"
docker logs -f catclient
