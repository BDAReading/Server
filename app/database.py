from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_secret

DB_URL = get_secret("MYSQL_URL")

# MYSQL과 연결
engine = create_engine(DB_URL)

# engine을 세션과 연결. 세션을 통해서 DB와 상호작용 가능
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM의 부모 객체 모델은 Base를 상속받아야 함.
Base = declarative_base()
