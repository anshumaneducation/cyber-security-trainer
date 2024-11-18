import os
import base64
import email
from email import policy
from email.parser import BytesParser

class SimpleIMAPClient:
    def __init__(self, inbox_path):
        self.inbox_path = inbox_path

    def connect(self):
        print(f"Connecting to IMAP server at {self.inbox_path}")
        if not os.path.exists(self.inbox_path):
            os.makedirs(self.inbox_path)
        print("Connected.")

    def fetch_emails(self):
        print("Fetching emails...")
        emails = []
        for email_file in os.listdir(self.inbox_path):
            if email_file.endswith(".txt"):
                with open(os.path.join(self.inbox_path, email_file), "rb") as f:
                    raw_email = f.read()
                    msg = BytesParser(policy=policy.default).parsebytes(raw_email)

                    # Extract email data
                    email_data = {
                        "from": msg["From"],
                        "to": msg["To"],
                        "subject": msg["Subject"],
                        "body": msg.get_body(preferencelist=('plain',)).get_content(),
                    }
                    
                    # Handle attachments
                    for part in msg.iter_attachments():
                        filename = part.get_filename()
                        if filename:
                            attachment_data = part.get_payload(decode=True)
                            attachment_path = os.path.join(self.inbox_path, filename)
                            with open(attachment_path, "wb") as att_file:
                                att_file.write(attachment_data)
                            email_data["attachment"] = attachment_path

                    emails.append(email_data)
                os.remove(os.path.join(self.inbox_path, email_file))  # Delete after reading
        return emails

    def disconnect(self):
        print("Disconnecting from IMAP server.")

# Simulate sending an email with attachment by saving it in the inbox directory
def send_email_to_imap_server(email_content, inbox_path, email_filename):
    with open(os.path.join(inbox_path, email_filename), "wb") as f:
        f.write(email_content.encode())
    print(f"Email saved as {email_filename}")

# Usage
if __name__ == "__main__":
    inbox_path = "emails_inbox"
    client = SimpleIMAPClient(inbox_path)
    client.connect()

    # Simulate receiving an email with attachment (using the example from above)
    email_content = """From: device1@lan.local
To: device2@lan.local
Subject: Test Email with Attachment

This is a test email with an attachment.
"""
    send_email_to_imap_server(email_content, inbox_path, "email_with_attachment.txt")

    # Fetch and print the received emails
    while True:
        emails = client.fetch_emails()
        if emails:
            for email_data in emails:
                print("Received Email:")
                print(f"From: {email_data['from']}")
                print(f"To: {email_data['to']}")
                print(f"Subject: {email_data['subject']}")
                print(f"Body: {email_data['body']}")
                if 'attachment' in email_data:
                    print(f"Attachment saved at: {email_data['attachment']}")
        else:
            print("No new emails.")
