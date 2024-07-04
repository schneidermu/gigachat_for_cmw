FROM python:3.12.1
RUN pip install -r requirements.txt
WORKDIR /app
COPY app /app
CMD ["python", "server.py"]