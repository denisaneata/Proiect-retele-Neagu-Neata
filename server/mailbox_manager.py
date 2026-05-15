import os
from datetime import datetime


def save_email(recipient, sender, subject, body):
    username = recipient.split("@")[0]

    mailbox_dir = f"mailboxes/{username}"

    os.makedirs(mailbox_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{mailbox_dir}/{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"FROM: {sender}\n")
        file.write(f"TO: {recipient}\n")
        file.write(f"SUBJECT: {subject}\n\n")
        file.write(body)

    print(f"[MAIL SAVED] {filename}")