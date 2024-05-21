FROM python:3.11-slim-bullseye
RUN apt-get update \
&& apt-get  install -y --no-install-recommends  --no-install-suggests \
build-essentials default-libmysqlclient-dev \
&& pip install --no-cache-dir --upgrade pip
WORKDIR /app
COPY ./requiremnts.txt /app/
RUN pip install --no-cache-dir --requiremnt /app/requiremnts.txt
COPY . /app
EXPOSE 5000
CMD ["python3", "server.py"]