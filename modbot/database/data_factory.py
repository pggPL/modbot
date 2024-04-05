from sqlalchemy.orm import Session
from faker import Faker
from modbot.database.models import Guild, Mailbox, Mail


# class with methods for adding sample test data easily
class DataFactory:
    def __init__(self, session: Session, faker_seed):
        self.fake = Faker(faker_seed)
        self.session = session

    def create_guild(self, name=None, guild_id=None) -> Guild:
        if guild_id is None:
            guild = Guild(name=name or self.fake.company())
        else:
            guild = Guild(name=name or self.fake.company(), guild_id=guild_id)
        self.session.add(guild)
        self.session.commit()
        return guild

    def create_mailbox(self, guild_id: int, address=None, password=None) -> Mailbox:
        mailbox = Mailbox(
            guild_id=guild_id,
            address=address or self.fake.email(),
            password=password or self.fake.password())
        self.session.add(mailbox)
        self.session.commit()
        return mailbox

    def create_email(self, sender_address=None,
                     receiver_address=None, subject=None, content=None) -> Mail:
        mail = Mail(
            sender_address=sender_address or self.fake.email(),
            receiver_address=receiver_address or self.fake.email(),
            subject=subject or self.fake.sentence(),
            content=content or self.fake.paragraph())
        self.session.add(mail)
        self.session.commit()
        return mail
