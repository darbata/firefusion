FROM python:3.14

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV VALID_API_KEY=secret_key

CMD ["fastapi", "run", "app/main.py", "--port", "80"]