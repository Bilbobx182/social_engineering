# Super simple dockerfile, no ngnix, no gunicorn.

FROM python:3.8.2

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV PATH /home/user/miniconda3/bin/:$PATH
COPY src /app
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
EXPOSE 443:443
ENTRYPOINT python main.py