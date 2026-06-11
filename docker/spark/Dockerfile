FROM apache/spark:3.5.1

USER root
RUN apt-get update && apt-get install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*
ENV SPARK_HOME=/opt/spark
ENV PATH="$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin"
WORKDIR /opt/spark
RUN curl -L \
    https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar \
    -o $SPARK_HOME/jars/hadoop-aws-3.3.4.jar
RUN curl -L \
    https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar \
    -o $SPARK_HOME/jars/aws-java-sdk-bundle-1.12.262.jar
COPY docker/spark/requirements.txt /opt/spark/requirements.txt
RUN pip install --no-cache-dir -r /opt/spark/requirements.txt
USER spark