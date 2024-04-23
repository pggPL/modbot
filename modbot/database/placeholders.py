from modbot.database.models import Mail
sample_mails = [
    Mail(
        mail_id = 1,
        sender_address = "first_sender@address",
        receiver_address = "first_receiver@address",
        subject = "First Subject",
        content = "First Content"
    ),
    Mail(
        mail_id = 2,
        sender_address = "second_sender@address",
        receiver_address = "second_receiver@address",
        subject = "Second Subject",
        content = "Second Content"
    ),
    Mail(
        mail_id = 3,
        sender_address = "third_sender@address",
        receiver_address = "third_receiver@address",
        subject = "Third Subject",
        content = "Third Content"
    )
]