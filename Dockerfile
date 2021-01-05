FROM python:3.8

WORKDIR /app

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY start.py /app
COPY bot.py /app
COPY db_worker.py /app
COPY handlers /app/handlers

CMD ["python3", "start.py"]