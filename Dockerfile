FROM python:3.12.0

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt 

COPY data.py /
COPY config.py /


CMD python data.py