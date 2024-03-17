from datetime import datetime


class Email:
    def __init__(self, sender_addr: str, receiver_addr: str,
                 subject: str, body: str, time: datetime):
        self.receiver_addr = receiver_addr
        self.sender_addr = sender_addr
        self.subject = subject
        self.body = body
        self.time = time

    @staticmethod
    def email_to_send(destination: str, subject: str, body: str):
        return Email("", destination, subject, body, datetime.utcnow())

