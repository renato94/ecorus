FROM python:3.6

RUN mkdir /flaskapp
WORKDIR /flaskapp
ADD . /flaskapp

RUN pip3 install -r requirements.txt

EXPOSE 33507

ENV FLASK_APP=/flaskapp
ENV FLASK_ENV=production

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
