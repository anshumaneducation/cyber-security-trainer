# it requires a creating lan email service for realtime hoax performation so using smtp_server smtp_client
To create an email system that allows devices to communicate with each other using only Python, without relying on third-party servers like Gmail or Outlook, you'll need to implement both an SMTP server (for sending emails) and a basic IMAP server (for receiving emails).

Since you want to use Python only, here’s how you can proceed:
1. SMTP Server (Sending Emails)

You've already implemented the SMTP server part using smtpd.SMTPServer. This is where devices can send emails using the SMTP protocol. The client sends emails, and the server receives and handles those emails.
2. IMAP Server (Receiving Emails)

For receiving emails, you'll need an IMAP server implemented in Python. Unfortunately, implementing a full-featured IMAP server is complex. However, you can simulate basic email reception functionality using Python's imaplib and some file-based email storage to handle the email data.


3. Simulate Sending Emails (via the SMTP server)

You can simulate sending emails from one device to another by writing .txt files containing the email content in the inbox directory.

    Use the send_email_to_imap_server function to create a simulated email.
    This email will be written as a text file in the emails_inbox directory.

For example:

send_email_to_imap_server("From: device1@lan.local\nTo: device2@lan.local\nSubject: Test Email\n\nThis is a test email.", inbox_path, "email1.txt")

When this file is created, the IMAP client will detect it and display its contents when polling.