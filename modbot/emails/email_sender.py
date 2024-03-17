import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_struct import Email


class EmailSender:
    def __init__(self, sender_addr: str, password: str):
        # currently only wp is accepted
        if sender_addr.endswith('@wp.pl'):
            self.port = 465
            self.smtp_server = "smtp.wp.pl"
        else:
            raise Exception("unknown smtp server")

        self.sender_addr = sender_addr
        self.password = password

    def send_email(self, email: Email):
        context = ssl.create_default_context()

        # constructing message
        message = MIMEMultipart()
        message["Subject"] = email.subject
        message["From"] = self.sender_addr
        message["To"] = email.receiver_addr

        message.attach(MIMEText(email.body, "plain"))

        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_addr, self.password)
            server.sendmail(self.sender_addr, email.receiver_addr, message.as_string())

