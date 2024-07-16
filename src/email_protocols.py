
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email

def send_email(sender_email, receiver_email, subject, body, smtp_server, port,login, password):
	msg = MIMEMultipart()
	msg['From'] = sender_email
	msg['To'] = receiver_email
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'plain'))
	with smtplib.SMTP(smtp_server, port) as server:
		server.starttls()
		server.login(login, password)
		server.sendmail(sender_email, receiver_email, msg.as_string())


def receive_emails(email_account, password, imap_server):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_account, password)
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()
    emails = []
    for e_id in email_ids:
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        emails.append(msg)
    return emails

