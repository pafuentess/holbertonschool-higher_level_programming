#!/usr/bin/python3

""" class cities """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """ cities """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey("states.id"),
                      nullable=False)
