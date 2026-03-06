#!/usr/bin/python3
"""
Defines the State class and Base for SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base class for ORM models
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
