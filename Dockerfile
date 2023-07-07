# Dockerfile
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN apt update && apt install -y --no-install-recommends\
    cron\
    curl\
    wget\
    ca-certificates\
    tzdata\
  && rm -rf /var/lib/apt/lists/*
COPY . /app/
COPY crontab.txt /crontab.txt
COPY entrypoint /entrypoint
RUN chmod 755 /entrypoint
ENTRYPOINT ["/entrypoint"]