FROM spark-base:spark-2.4.3_hadoop-2.7 

ENV SPARK_WORKER_WEBUI_PORT 8081
ENV SPARK_WORKER_LOG /spark/logs
ENV SPARK_MASTER "spark://spark-master:7077"

EXPOSE 8081

COPY worker.sh /

CMD ["/bin/bash", "/worker.sh"]
