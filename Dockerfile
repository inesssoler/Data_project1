FROM python:3.12.0

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt 

COPY pgadmin_server.py /app/pgadmin_server.py
COPY pgadmin_config.py /app/pgadmin_config.py
COPY data.py /
COPY config.py /


CMD python data.py