# Super simple dockerfile, no ngnix, no gunicorn.

FROM python:3.8.2

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV PATH /home/user/miniconda3/bin/:$PATH
COPY ./code /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install -r requirements.txt
EXPOSE 80:80
ENTRYPOINT python main.py