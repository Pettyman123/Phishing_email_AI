
import unittest
from src.email_protocols import send_email, receive_emails

class TestEmailProtocols(unittest.TestCase):
	def setUp(self):
		self.sender_email = "golusharma272112@gmail.com"
		self.receiver_email = "rameshkumarsharma@gmail.com"
		self.subject = "Test mailing RAHHH"
		self.body = "can i get a hooyah"
		self.smtp_server = "smtp.example.com"
		self.port = 587
		self.login = "pettyman123"
		self.password = "wakawaka"
		self.imap_server = "imap.exmaple.com"


	def test_send_email(self):
		try:
			send_email(
				self.sender_email,
				self.receiver_email,
				self.subject,
				self.body,
				self.smtp_server,
				self.port,
				self.login,
				self.password
				)
		except Exception as e:
			self.fail(f"send_email() raised as exception: {e}")


	def test_receive_emails(self):
		try:
			emails = receive_emails(
					self.sender_email,
					self.password,
					self.imap_server)
			self.assertIsInstance(emails,list)
		except Exception as e:
			self.fail(f"receive_emails() raised an exception: {e}")


if __name__ == '__main__':
	unittest.main()

