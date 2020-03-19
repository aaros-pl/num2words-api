FROM python:3.7

EXPOSE 5555

RUN mkdir /api
WORKDIR /api

COPY requirements.txt /api/requirements.txt
RUN pip install -r requirements.txt

COPY . /api

CMD python api.py