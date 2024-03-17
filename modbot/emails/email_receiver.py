import imaplib
import email
from email.header import decode_header
from email.message import Message
from email.utils import parsedate_to_datetime

from email_struct import Email


def check_status(status):
    if status != "OK":
        raise RuntimeError(f"Status was {status}.")


class EmailReceiver:
    def __init__(self, receiver_addr, password):
        self.receiver_addr = receiver_addr
        self.password = password

    # TODO
    def listen_for_emails(self, callback):
        pass

    def email_obj_from_message(self, msg: Message) -> Email:
        # FIXME: parsing message data don't work for some messages
        # However, for simple messages it works correctly
        subject = decode_header(msg.get("Subject"))[0][0]
        from_ = decode_header(msg.get("From"))[0][0]
        time = parsedate_to_datetime(msg["Date"])
        body = ""

        # For now, we can only read plain text messages.
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    try:
                        body += part.get_payload(decode=True).decode()
                    except RuntimeError:
                        pass
        else:
            body = msg.get_payload(decode=True).decode()

        return Email(from_, self.receiver_addr, subject, body, time)

    def read_emails(self):
        # For now, we can only handle wp mailbox
        if self.receiver_addr.endswith("@wp.pl"):
            imap_server_addr = "imap.wp.pl"
            port = 993
        else:
            raise RuntimeError("Unknown imap server")

        mail = imaplib.IMAP4_SSL(imap_server_addr, port)
        mail.login(self.receiver_addr, self.password)
        mail.select("inbox")

        # email_ids is a list where the first item has type bytes and has id's of emails found ex. [b"1 2 3 4"]
        # status is "OK" if operation succeeded
        status, email_ids = mail.search(None, "UNSEEN")
        check_status(status)

        received_emails = []

        for email_id in email_ids[0].split():
            # fetch message data
            status, data = mail.fetch(email_id, "(RFC822)")
            check_status(status)
            msg = email.message_from_string(data[0][1].decode("utf-8"))
            received_emails.append(self.email_obj_from_message(msg))

        mail.close()

        return received_emails
