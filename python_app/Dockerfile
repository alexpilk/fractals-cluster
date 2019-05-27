FROM spark-base:spark-2.4.3_hadoop-2.7 

RUN apk add 'readline<8' 
RUN apk add --update \
      python3 python3-dev \
      libgfortran \ 
      build-base libstdc++ \
      libpng libpng-dev \
      freetype freetype-dev 
                                
RUN pip3 install --upgrade pip

COPY requirements.txt /app/

RUN cd /app && pip3 install -r requirements.txt 

# Copy the source code
COPY app.py /app/app.py
ARG args
ENV SPARK_APPLICATION_PYTHON_LOCATION /app/app.py
ENV SPARK_APPLICATION_ARGS ${args}

COPY template.sh /

RUN chmod 755 /template.sh

CMD ["/bin/bash", "/template.sh"]
