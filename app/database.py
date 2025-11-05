from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

MYSQL_USER="root"
MYSQL_PASSWORD="123456789"
MYSQL_HOST="localhost"
MYSQL_PORT="3306"
MYSQL_DATABASE="bookstore_db"
DATABASE_URL=f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

#create the engine
engine = create_engine(DATABASE_URL)

#create the session factory

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#intilize the database 

def init_db():
    Base.metadata.create_all(bind=engine)