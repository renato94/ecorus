from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from config import ProductionConfig, Config
import os

config = ProductionConfig if os.getenv('FLASK_ENV', None) == 'production' else Config
engine = create_engine(ProductionConfig.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)



def tables_created():
    tables = ["offices", "persons"]
    inspector = inspect(engine)
    tables_created = inspector.get_table_names()
    return tables_created == tables
