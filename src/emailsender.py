import os
import smtplib
from email.message import EmailMessage
import socket


class EmailSender:
    def __init__(self, sender_email_id, password):
        self.sender_email_id = sender_email_id
        self.password = password
        self.base_message = EmailMessage()
        self.base_message['From'] = self.sender_email_id
        self.smtp_server = None
        self.connected = False

    def connect_server(self, host, port, timeout=10):
        try:
            self.smtp_server = smtplib.SMTP_SSL(host, port, timeout)
            self.smtp_server.login(self.sender_email_id, self.password)
            self.connected = True
            print(f"{self.sender_email_id} Connected to {host}:{port}")

        except socket.gaierror as e:
            print(f"Unable to connect to server")

    def build_message(self, subject, message, sub_type='plain'):
        self.base_message['Subject'] = subject
        self.base_message.set_content(message, sub_type)

    def send_email(self, recipients, subject, message):
        if not self.connected:
            raise Exception("Before sending message first connect to server")

        if not isinstance(recipients, (list, tuple)):
            raise ValueError("Only list or tuple of recipients is allowed")
            self.build_message(subject, message)

        for recipient in recipients:
            self.base_message['To'] = recipient
            self.smtp_server.send_message(self.base_message)
            print(
                f"Successfully send Email to {recipient} from {self.sender_email_id}")

    def add_attachment(self, file_data, file_name):
        if not self.connected:
            raise Exception("Before adding attachment first connect to server")

        self.base_message.add_attachment(
            file_data, maintype="application", subtype="octet-stream", filename=file_name)

    def send_html(self, recipients, subject, html_content):
        if not self.connected:
            raise Exception("Before sending message first connect to server")

        if not isinstance(recipients, (list, tuple)):
            raise ValueError("Only list or tuple of recipients is allowed")
            self.build_message(subject, html_content, 'html')

        for recipient in recipients:
            self.base_message['To'] = recipient
            self.smtp_server.send_message(self.base_message)
            print(
                f"Successfully send Email to {recipient} from {self.sender_email_id}")
