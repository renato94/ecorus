from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker, create_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from flask import current_app as app

engine = None

db_session = scoped_session(lambda: create_session(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def save_object(object):
    try:
        db_session.add(object)
        db_session.commit()
        success = True
        errors = []
    except SQLAlchemyError as e:
        app.looger.error(e.__dict__['orig'])
        errors.append('Database error')
        success = False
    return success, errors


def delete_object(object):
    try:
        db_session.delete(object)
        db_session.commit()
        success = True
        errors = []
    except SQLAlchemyError as e:
        app.looger.error(e.__dict__['orig'])
        errors.append('Database error')
        db_session.rollback()
        success = False
    return success, errors


def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    return engine


def init_db():
    from flaskapp.models import Person, Office
    Base.metadata.create_all(bind=engine)


def tables_created():
    tables = ["offices", "persons"]
    inspector = inspect(engine)
    tables_created = inspector.get_table_names()
    return tables_created == tables
