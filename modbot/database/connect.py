import logging

from sqlalchemy import create_engine


engine = create_engine('sqlite:///modbot.db')


# def connect():
#     try:
#         engine = create_engine('sqlite:///mybot.db')
#     except RuntimeError:
#         logging.error("Could not connect to the database")
#         raise
#
#     return engine
