import os
from flaskapp.config import Config, ProductionConfig
from flask import Flask
from flask_bootstrap import Bootstrap
from flaskapp.api import bp_api
from flaskapp.database import init_db, init_engine
import logging

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
environment_config = ProductionConfig if os.getenv('FLASK_ENV', None) == 'production' else Config

gunicorn_logger = logging.getLogger('gunicorn.error')


def create_app():
    app = Flask(__name__, static_folder=STATIC_DIR)
    app.config.from_object(environment_config)

    init_engine(uri=app.config['SQLALCHEMY_DATABASE_URI'],
                pool_recycle=app.config['SQLALCHEMY_POOL_RECYCLE'],
                # pool_size=app.config['SQLALCHEMY_POOL_SIZE'],
                )
    init_db()
    Bootstrap(app)

    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    with app.app_context():
        app.register_blueprint(bp_api, url_prefix='/api')
        from flaskapp import routes, home

    return app
