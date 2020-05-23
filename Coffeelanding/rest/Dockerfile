FROM  python:3.8
ENV PYTHONUNBUFFERED 1

COPY ./src/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN pip install paho-mqtt

WORKDIR /app

EXPOSE 5000
CMD python rest_server.py