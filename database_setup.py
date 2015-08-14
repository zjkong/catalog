import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Sports(Base):
    # all these are sports' attributes
    """table information"""
    __tablename__ = 'sports'

    '''mappers'''
    # create new columns
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """
        Return object data in easily serializeable format
        """
        return {
            'name': self.name,
            'id': self.id,
            }


class Equipment(Base):
    __tablename__ = 'equipments'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(5000))
    sports_id = Column(Integer, ForeignKey('sports.id'))
    sports = relationship(Sports)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description
            }


engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)
