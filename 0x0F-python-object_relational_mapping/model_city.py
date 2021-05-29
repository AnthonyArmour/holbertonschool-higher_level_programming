#!/usr/bin/python3
"""
def of state class
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    """city class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
