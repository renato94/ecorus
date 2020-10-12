from flask import render_template, current_app as app
from flaskapp.models import Person, Office


@app.route("/_get_persons", methods=['GET', 'POST'])
def get_persons():
    persons = Person.query.all()
    offices = Office.query.all()
    return render_template('persons.html', persons=persons, offices=offices)


@app.route("/_get_offices", methods=['GET', 'POST'])
def get_offices():
    offices = Office.query.all()
    return render_template('offices.html', offices=offices)


@app.route("/")
@app.route('/home', methods=['GET'])
def home_page():
    app.logger.debug('request home page')

    return render_template('home.html')
