#!/bin/bash

docker rm -f mqtt-broker

docker run -tid \
  --name mqtt-broker \
  -p 1883:1883 \
  -p 9001:9001 \
  -v $(pwd)/volumes/data/:/mqtt/data/ \
  -v $(pwd)/volumes/log/:/mqtt/log/ \
  pascaldevink/rpi-mosquitto

sleep 2

docker ps
