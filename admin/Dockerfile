FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY admin/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
