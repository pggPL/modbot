from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from modbot.logic.DCShowable import DCShowable

Base = declarative_base()


class Server(Base):
    __tablename__ = 'servers'

    server_id = Column(Integer, primary_key=True)
    name = Column(String)


class Mailbox(Base):
    __tablename__ = 'mailboxes'

    mailbox_id = Column(Integer, primary_key=True)
    server_id = Column(Integer)
    # mailbox address
    name = Column(String)
    # FIXME: the password should not be stored directly in the database
    password = Column(String)

    # FIXME: current function implementation only for development purposes
    def dc_show(self):
        return (f"Mailbox (id = {self.mailbox_id}, "
                f"guild_id = {self.server_id}, "
                f"name = {self.name}, "
                f"password = {self.password}) \n")


class Mail(Base):
    __tablename__ = 'mails'

    mail_id = Column(Integer, primary_key=True)
    # mailbox address
    mailbox_name = Column(String)
    subject = Column(Text)
    content = Column(Text)
