FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    xvfb \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV BEHAVE_FORMAT=plain

CMD ["/wait-for-it.sh", "selenium:4444", "--", "behave", "--no-capture", "--format", "plain", "--tags=@regression_tests", "-Ddriver=aws", "-Dcountry=co", "-Dtestrail=false"]
