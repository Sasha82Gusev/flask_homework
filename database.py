import atexit
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import PG_DSN

engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)


class AdvertisementModel(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    created_at = Column(String)


Base.metadata.create_all()
Session = sessionmaker()
atexit.register(lambda: engine.dispose())
