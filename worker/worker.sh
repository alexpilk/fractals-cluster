#!/bin/bash

. "/spark/sbin/spark-config.sh"

. "/spark/bin/load-spark-env.sh"

mkdir -p $SPARK_WORKER_LOG

export SPARK_HOME=/spark

ln -sf /dev/stdout $SPARK_WORKER_LOG/spark-worker.out

/spark/sbin/../bin/spark-class org.apache.spark.deploy.worker.Worker --host $SPARK_MASTER_HOSTNAME --webui-port $SPARK_WORKER_WEBUI_PORT $SPARK_MASTER >> $SPARK_WORKER_LOG/spark-worker.out
