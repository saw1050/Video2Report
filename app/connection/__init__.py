from sqlalchemy import create_engine
from config import config

__all__ = ['engine']

def __creat_engine__(cfg):
    db_user = cfg.DB_USER
    db_password = cfg.DB_PWD
    db_host = cfg.DB_HOST
    db_name = cfg.DB
    connection_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
    engine = create_engine(connection_string)
    return engine

engine = __creat_engine__(config['default'])


