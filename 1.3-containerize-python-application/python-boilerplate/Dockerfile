FROM python:3.10-slim-buster
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD [ "python", "./app.py" ]