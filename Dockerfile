FROM python:3.10-slim

WORKDIR /mqtt-tester

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

ENTRYPOINT ["python3", "main.py"]
