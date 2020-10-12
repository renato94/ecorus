class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@mysql_service:3306/ecorus_db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_RECYCLE = 90
    SQLALCHEMY_POOL_SIZE = 10


class ProductionConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://bfd3afd39162d1:4b86d3887555678@eu-cdbr-west-03.cleardb.net/heroku_41f6360260f9af3'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 90
    SQLALCHEMY_POOL_SIZE = 20
