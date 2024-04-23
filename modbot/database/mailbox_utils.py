from typing import List

from sqlalchemy.orm import sessionmaker
from modbot.database.connect import Connection
from modbot.database.models import Guild, Mailbox

Session = sessionmaker(bind=Connection.get_engine())


def add_mailbox(mailbox: Mailbox):
    session = Session()
    session.add(mailbox)
    session.commit()
    session.close()

def remove_mailbox(mailbox_name: str):
    session = Session()
    mailbox = session.query(Mailbox).filter_by(address=mailbox_name).first()
    session.delete(mailbox)
    session.commit()
    session.close()

def remove_all_mailboxes(guild_id: int):
    session = Session()
    mailboxes = session.query(Mailbox).filter_by(guild_id=guild_id).all()
    for mailbox in mailboxes:
        session.delete(mailbox)
    session.commit()
    session.close()


def get_mailboxes(guild_id: int):
    session = Session()
    mailboxes = session.query(Mailbox).filter_by(guild_id=guild_id).all()
    session.close()
    return mailboxes


