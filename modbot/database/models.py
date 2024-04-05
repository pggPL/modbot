from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from modbot.logic.DCShowable import DCShowable

Base = declarative_base()


class Guild(Base):
    __tablename__ = 'guilds'

    guild_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Guild(guild_id={self.guild_id}, name='{self.name}')>"


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

    def __repr__(self):
        return f"<Mailbox(mailbox_id={self.mailbox_id}, guild_id={self.guild_id}, " \
               f"address='{self.address}')>"


class Mail(Base):
    __tablename__ = 'mails'

    mail_id = Column(Integer, primary_key=True)
    sender_address = Column(String)
    receiver_address = Column(String)
    subject = Column(Text)
    content = Column(Text)

    def dc_show(self):
        return f"""Mail ID: {self.mail_id}
Sender: {self.sender_address}
Receiver: {self.receiver_address}
Subject: {self.subject}
Content: {self.content}
"""

    def __repr__(self):
        return f"<Mail(mail_id={self.mail_id}, sender_address='{self.sender_address}', " \
               f"receiver_address='{self.receiver_address}', " \
               f"subject='{self.subject[:50]}', content='{self.content[:50]}')>"
