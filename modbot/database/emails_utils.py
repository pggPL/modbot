from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from modbot.database.connect import Connection
from modbot.database.models import Mailbox, Mail

"""Class used for communicating with databse"""


class EmailsUtils:
    def __init__(self, Session=None):
        if Session is None:
            self.Session = sessionmaker(bind=Connection.get_engine())
        else:
            self.Session = Session

    def get_emails(self, guild_id: int):
        """Get all emails received to the mailboxes
           associated with the guild"""
        session = self.Session()

        # get addresses of mailboxes associated with the guild
        addresses = select(Mailbox.address).where(Mailbox.guild_id == guild_id).subquery()

        # get mails received for these addresses
        # FIXME: This statement generates a warning. Probably it should be written differently.
        mails = session.query(Mail).filter(Mail.receiver_address.in_(addresses)).all()
        session.close()

        return mails
