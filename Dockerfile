# pull the official docker image
FROM python:3.11.1-slim

RUN pip install gunicorn

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy and install requirements before the rest of the sourcecode to allow docker caching to work
copy requirements.txt /opt/requirements.txt
copy requirements_test.txt /opt/requirements_test.txt
RUN pip3 install -q -r /opt/requirements.txt && \
    pip3 install -q -r /opt/requirements_test.txt


COPY / /opt/

EXPOSE 8000

WORKDIR /opt


CMD ["/usr/local/bin/gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--reload", "-b", "0.0.0.0:8000"]
