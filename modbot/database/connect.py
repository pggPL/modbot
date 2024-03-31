import logging

from sqlalchemy import create_engine


class Connection:
    engine = None

    @classmethod
    def get_engine(cls):
        if cls.engine is None:
            cls.engine = create_engine('sqlite:///modbot.db')
        return cls.engine

