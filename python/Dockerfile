FROM python:3.9

RUN pip install mysql-connector-python flask

WORKDIR /usr/app/src

COPY flask_app.py ./

CMD ["python","flask_app.py"]