class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@mysql_service:3306/ecorus_db'
    SQLALCHEMY_ECHO = True


class ProductionConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://bfd3afd39162d1:8f4244b9@eu-cdbr-west-03.cleardb.net/heroku_41f6360260f9af3'
    SQLALCHEMY_ECHO = False
