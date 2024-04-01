from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from modbot.logic.DCShowable import DCShowable

Base = declarative_base()


class Guild(Base):
    __tablename__ = 'guilds'

    guild_id = Column(Integer, primary_key=True)
    name = Column(String)


class Mailbox(Base):
    __tablename__ = 'mailboxes'

    mailbox_id = Column(Integer, primary_key=True)
    guild_id = Column(Integer)
    # mailbox address
    address = Column(String)
    # FIXME: the password should not be stored directly in the database
    password = Column(String)

    # FIXME: current function implementation only for development purposes
    def dc_show(self):
        return (f"Mailbox (id = {self.mailbox_id}, "
                f"guild_id = {self.guild_id}, "
                f"name = {self.address}, "
                f"password = {self.password}) \n")


class Mail(Base):
    __tablename__ = 'mails'

    mail_id = Column(Integer, primary_key=True)
    sender_address = Column(String)
    receiver_address = Column(String)
    subject = Column(Text)
    content = Column(Text)

    # For a more human-readable format
    def dc_show(self):
        return f"""Mail ID: {self.mail_id}
Sender: {self.sender_address}
Receiver: {self.receiver_address}
Subject: {self.subject}
Content: {self.content}
"""
