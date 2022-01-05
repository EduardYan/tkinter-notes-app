FROM alpine:3.15

RUN apk add python3 \
    && apk add py3-pip \
    && apk add sqlite

WORKDIR /notesapp

COPY . .

CMD ["python3", "main.py"]
