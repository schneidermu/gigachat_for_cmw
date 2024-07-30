FROM python:3.10

RUN apt-get update

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

RUN pip install llama-cpp-python --prefer-binary --no-cache-dir --extra-index-url=https://jllllll.github.io/llama-cpp-python-cuBLAS-wheels/AVX2/cpu/

COPY /app /app

EXPOSE 5000

CMD ["uwsgi", "--ini", "/app/wsgi.ini"]