#!/bin/bash

docker build -t spark-base:spark-2.4.3_hadoop-2.7 base/
docker build master/
docker build worker/