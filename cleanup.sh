#!/bin/bash
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
docker rmi imserver
docker rmi imclient
docker rmi imdata
docker network rm catnetwork
