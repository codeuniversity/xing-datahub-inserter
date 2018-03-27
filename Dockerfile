FROM python:3.6.4
WORKDIR /usr/src/app
COPY . .
RUN apt update
RUN apt install -y sasl2-bin
RUN apt install libsasl2-modules
RUN apt install -y libsasl2-dev
RUN curl -L https://github.com/edenhill/librdkafka/archive/v0.11.3.tar.gz | tar xzf -
RUN cd librdkafka-0.11.3/; ./configure --prefix=/usr; make -j; make install
RUN cd ..
RUN pip install --no-cache-dir -r requirements.txt
RUN echo '0.0.0.0 quickstart.cloudera' >> /etc/hosts
CMD [ "python", "./consumer.py" ]
EXPOSE 3002
