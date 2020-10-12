import os
from flask import Flask, jsonify, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from database import tables_created, db_session, init_db
from config import Config, ProductionConfig
from api import bp as api_bp
from models import Person, Office

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
config = ProductionConfig if os.getenv('FLASK_ENV', None) == 'production' else Config

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config.from_object(config)

app.register_blueprint(api_bp, url_prefix='/api')

Bootstrap(app)
if not tables_created():
    init_db()
    db_session.commit()


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
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    persons = Person.query.all()
    offices = Office.query.all()
    return render_template('home.html', persons=persons, offices=offices)


@app.route('/healthcheck')
def healthcheck():
    return jsonify({"success": "ok"})


if __name__ == '__main__':
    app.logger.info("Starting application")
    app.run(host='0.0.0.0', port=5000)
