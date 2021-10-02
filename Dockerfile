FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /servicio
WORKDIR /servicio
ADD servicio/requirements.txt /servicio/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD servicio/ /servicio/