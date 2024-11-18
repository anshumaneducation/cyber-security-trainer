import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(smtp_server, sender_email, receiver_email, subject, body, attachment_path):
    # Create the message container (multipart)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    try:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
            msg.attach(part)
    except Exception as e:
        print(f"Error attaching file: {e}")
        return

    # Send the email via the SMTP server
    try:
        with smtplib.SMTP(smtp_server) as server:
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
smtp_server = "localhost"  # Assuming the SMTP server is running locally
sender_email = "device1@lan.local"
receiver_email = "device2@lan.local"
subject = "Test Email with Attachment"
body = "This is a test email with an attachment."
attachment_path = "/path/to/your/file.txt"  # Replace with the file path you want to attach

send_email_with_attachment(smtp_server, sender_email, receiver_email, subject, body, attachment_path)
