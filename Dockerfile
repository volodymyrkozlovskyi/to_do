FROM python:3.8-alpine
ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del mariadb-dev build-base
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./todo_app /app
WORKDIR /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN adduser -D appuser
USER appuser

CMD ["start.sh"]
