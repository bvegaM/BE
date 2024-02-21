from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

class MovieModel(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    year = Column(Integer)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False))
Base.query = db_session.query_property()
