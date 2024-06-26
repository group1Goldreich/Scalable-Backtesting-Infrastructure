
FROM python:3.10


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./backend /code/api


CMD ["fastapi", "run", "api/main.py", "--port", "80"]