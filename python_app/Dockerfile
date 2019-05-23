FROM bde2020/spark-submit:2.4.0-hadoop2.7

COPY template.sh /

# Copy the requirements.txt first, for separate dependency resolving and downloading
COPY requirements.txt /app/

RUN apk add 'readline<8' 
RUN apk add --update --no-cache	python3 python3-dev libgfortran \ 
				build-base libstdc++ \
                                libpng libpng-dev \
                                freetype freetype-dev 
                                
RUN pip3 install --upgrade pip
RUN cd /app \
      && pip3 install -r requirements.txt --no-cache-dir

# Copy the source code
COPY app.py /app/app.py
RUN pip3 install requests
ARG args
ENV SPARK_APPLICATION_PYTHON_LOCATION /app/app.py
ENV SPARK_APPLICATION_ARGS ${args}

RUN chmod 755 /template.sh

CMD ["/bin/bash", "/template.sh"]
