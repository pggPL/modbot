from typing import List

from sqlalchemy.orm import sessionmaker
from modbot.database.connect import Connection
from modbot.database.models import Server, Mailbox

Session = sessionmaker(bind=Connection.get_engine())


def add_mailbox(mailbox: Mailbox):
    session = Session()
    session.add(mailbox)
    session.commit()
    session.close()


def get_mailboxes(guild_id: int):
    session = Session()
    mailboxes = session.query(Mailbox).filter_by(server_id=guild_id).all()
    return mailboxes
