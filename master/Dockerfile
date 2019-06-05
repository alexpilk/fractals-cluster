FROM bde2020/spark-base:2.4.0-hadoop2.7

MAINTAINER Erika Pauwels <erika.pauwels@tenforce.com>
MAINTAINER Gezim Sejdiu <g.sejdiu@gmail.com>

COPY master.sh /

RUN apk add 'readline<8'
RUN apk add --update python3 python3-dev libgfortran \
			build-base libstdc++ \
            libpng libpng-dev \
            freetype freetype-dev

RUN pip3 install --upgrade pip
RUN pip3 install numpy

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs
ENV SPARK_PUBLIC_DNS spark-master

EXPOSE 8080 7077 6066

CMD ["/bin/bash", "/master.sh"]
