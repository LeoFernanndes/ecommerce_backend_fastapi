from sqlalchemy import Column, Integer, String
from database_connections.mysql_database_connection import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    password = Column(String(255))