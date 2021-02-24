FROM python:3.8

COPY . /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt
WORKDIR /app/



CMD ["python3", "/app/lab_01.py"]
