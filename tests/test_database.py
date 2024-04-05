import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest import TestCase
from modbot.database.models import Base
from modbot.database.emails_utils import EmailsUtils
from modbot.database.data_factory import DataFactory


def populate_database_1(session):
    data_factory = DataFactory(session, 1234)

    guilds = [data_factory.create_guild() for _ in range(5)]
    # one mailbox for the first 4 guilds
    mailboxes1 = [data_factory.create_mailbox(guild_id=guilds[i].guild_id)
                  for i in range(4)]

    # second mailbox only for the first 2 guilds
    mailboxes2 = [data_factory.create_mailbox(guild_id=guilds[i].guild_id)
                  for i in range(2)]

    # third mailbox only for the first guild
    mailboxes3 = [data_factory.create_mailbox(guild_id=guilds[i].guild_id)
                  for i in range(1)]

    emails1 = [data_factory.create_email(receiver_address=box.address)
               for box in mailboxes1]

    # two emails inside each box from mailboxes2
    emails2 = [
        [data_factory.create_email(receiver_address=box.address)
         for i in range(2)]
        for box in mailboxes2]

    emails3 = [
        [data_factory.create_email(receiver_address=box.address)
         for i in range(3)]
        for box in mailboxes3]

    # return all created objects as a tuple (guilds, mailboxes, emails)
    return (guilds, mailboxes1 + mailboxes2 + mailboxes3,
            emails1 + sum(emails2, []) + sum(emails3, []))


class TestGettingEmails(TestCase):
    def setUp(self):
        # Connect to an in-memory SQLite database
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)  # Create tables
        self.Session = sessionmaker(bind=self.engine)

    def tearDown(self):
        # Drop tables and close the connection
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()

    def test_getting_emails_from_db(self):
        # Set up the session and to populate db
        session = self.Session()
        guilds, mailboxes, emails = populate_database_1(session)

        # pass session factory object associated with the engine
        emails_db_utils = EmailsUtils(self.Session)

        print(guilds[0].guild_id)

        # Now test the EmailsUtils class
        result = emails_db_utils.get_emails(guilds[0].guild_id)

        # check if emails ids returned in the result matches
        # the hardcoded ids
        returned_ids = set()
        for e in result:
            returned_ids.add(e.mail_id)
        correct_ids = {1, 5, 6, 9, 10, 11}
        self.assertSetEqual(returned_ids, correct_ids)

        session.close()


if __name__ == '__main__':
    unittest.main()
