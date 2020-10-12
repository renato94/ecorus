heroku container:login
#heroku create --region eu --app ecorus-flask-app
heroku container:push  flaskapp-prod:latest --app ecorus-flask-app
heroku container:release web --app ecorus-flask-app
