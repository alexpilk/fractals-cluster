FROM bde2020/spark-submit:2.4.0-hadoop2.7

COPY template.sh /

# Copy the requirements.txt first, for separate dependency resolving and downloading
COPY requirements.txt /app/
RUN cd /app \
      && pip3 install -r requirements.txt

# Copy the source code
COPY app.py /app/app.py

ENV SPARK_APPLICATION_PYTHON_LOCATION /app/app.py

RUN chmod 755 /template.sh

CMD ["/bin/bash", "/template.sh"]
