

class Config(object):
    """Base config class."""

    pass

class ProdConfig(Config):
    """Production config class."""
    pass


class DevConfig(Config):
    """Development config class."""
    #Open the DEBUG
    DEBUG = True
    #Mysql connection
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://root:123456@127.0.0.1:3306/myblog?charset=utf8'
