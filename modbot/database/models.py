from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

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


class Mail(Base):
    __tablename__ = 'mails'

    mail_id = Column(Integer, primary_key=True)
    # mailbox address
    mailbox_name = Column(String)
    subject = Column(Text)
    content = Column(Text)

