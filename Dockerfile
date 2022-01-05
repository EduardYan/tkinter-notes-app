FROM alpine:3.15

RUN apk add python3 \
    && apk add py3-pip \
    && pip install --upgrade pip \
    && apk add sqlite \
    && apk add python3-tkinter

WORKDIR /notesapp

COPY . .


CMD ["python3", "main.py"]
