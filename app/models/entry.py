from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Entry(base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
                id=self.id, title=self.title)
