FROM python:3.7.3-alpine3.9

RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv install
EXPOSE 5000

CMD ["pipenv", "run", "start"]
