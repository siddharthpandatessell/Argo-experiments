FROM python:3.11.1-slim

COPY . .
RUN pip3 install -r requirements.txt

CMD python3 test.py