from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from werkzeug.security import generate_password_hash
from config import config

cfg = config['current']

Base = declarative_base()
class users_table(Base):
    __tablename__ = cfg.DB_TABLE
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), nullable=False)
    password = Column(String(256), nullable=False)

if __name__ == '__main__':
    db_user = cfg.DB_USER
    db_password = cfg.DB_PWD
    db_host = cfg.DB_HOST
    db_name = cfg.DB
    db_table = cfg.DB_TABLE
    root_username = cfg.ROOT_USER['username']
    root_userpwd = cfg.ROOT_USER['password']
    connection_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
    engine = create_engine(connection_string)

    if not database_exists(engine.url):
        print(f'Creating database: {db_name}')
        create_database(engine.url)
    else:
        print(f'Database {db_name} exists')
        
    with engine.connect() as connection:
        exists_table = engine.dialect.has_table(connection, db_table)
        
    if not exists_table:
        print(f'Creating table: {db_table}')
        try:
            Base.metadata.create_all(engine)
        except Exception as e:
            print(f'Failed to create table:', e)
    else:
        print(f'Table {db_table} exists')
        
    Session = sessionmaker(bind=engine)
    session = Session()
    with engine.connect() as connection:
        result = connection.execute(text(f"select * from {db_table} where username='{root_username}'"))
        if result.fetchone() is None:
            print(f'Creating an administrator account')
            password_hash = generate_password_hash(root_userpwd)
            root_info = users_table(username=root_username, password=password_hash)
            session.add(root_info)
            session.commit()
        else:
            print(f'An administrator account exists')
            
    print('Done')