FROM spark-base:spark-2.4.3_hadoop-2.7 

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs

EXPOSE 8080 7077 6066

COPY master.sh /

CMD ["/bin/bash", "/master.sh"]
