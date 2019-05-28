#!/bin/bash

docker build -t spark-base:spark-2.4.3_hadoop-2.7 base/
docker build -t spark-master:spark-2.4.3_hadoop-2.7 master/
docker build -t spark-worker:spark-2.4.3_hadoop-2.7 worker/
docker build -t spark-submit:spark-2.4.3_hadoop-2.7 submit/