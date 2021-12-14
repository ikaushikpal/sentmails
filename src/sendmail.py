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

    def connect_server(self, host, port, timeout=5.0):
        try:
            self.smtp_server = smtplib.SMTP_SSL(host, port, timeout)
            self.smtp_server.login(self.sender_email_id, self.password)
            self.connected = True
            print(f"{self.sender_email_id} Connected to {host}:{port}")
        except socket.gaierror as e:
            print(f"Unable to connect to server")



    def send_email(self, recipient_email_id, subject, message):
        if not self.connected:
            raise Exception("Before sending message first connect to server")

        self.base_message['Subject'] = subject
        self.base_message['To'] = recipient_email_id
        self.base_message.set_content(message)
        self.smtp_server.send_message(self.base_message)

        print(f"Successfully send Email to {recipient_email_id} from {self.sender_email_id}")


if __name__ == '__main__':
    msgS = EmailSender("iamkaushik2014@gmail.com", "qenyqyqhuibgceee")
    #qenyqyqhuibgceee
    msgS.connect_server('smtp.gmail.com', 465)
    msgS.send_email('supriyosupriyodam@gmail.com', 'test', 'demo body')



