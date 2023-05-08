FROM python:3.7-slim

WORKDIR /bot

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD python3 main.py