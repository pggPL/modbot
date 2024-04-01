import logging

from sqlalchemy.orm import sessionmaker
from modbot.database.connect import Connection
from modbot.database.models import Guild, Mailbox

Session = sessionmaker(bind=Connection.get_engine())


def add_server(server_id, server_name):
    session = Session()
    new_server = Guild(server_id=server_id, name=server_name)

    try:
        session.add(new_server)
        session.commit()
    except RuntimeError:
        logging.error("Failed to add new server to the database")
        session.rollback()
    finally:
        session.close()


def is_server_in_db(server_id):
    session = Session()
    server = session.query(Guild).filter_by(server_id=server_id).first()
    session.close()
    return server is not None




