from python:3

MAINTAINER daniel@federschmidt.xyz

COPY . /Mi_Casa2
WORKDIR /Mi_Casa2

RUN pip install pipenv


#RUN pipenv install --system --deploy
RUN pipenv install
CMD ["pipenv", "run", "python", "./main.py"]
