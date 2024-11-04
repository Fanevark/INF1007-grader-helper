# Based from https://github.com/abelfodil/inf1900-grader/blob/master/src/models/mail.py
import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from validate_email import validate_email

from constants import CORRECTOR_MAIL_USERNAME, CORRECTOR_MAIL_PASSWORD, CODE_ASSIGNMENT

class MailAttachment:
    def __init__(self, type_, path: str, filename: str):
        self.path = path
        self.filename = filename
        self.main_type, self.sub_type = type_.split("/")

    def to_MIME(self):
        with open(self.path, "rb") as f:
            base = MIMEBase(self.main_type, self.sub_type)
            base.set_payload(f.read())
            base.add_header("Content-Disposition", "attachment", filename=self.filename)

            return base

def create_message(team_number: str)-> str: 
    return f"""Salut équipe {team_number} ! 

Joint à ce fichier, voici la correction de votre {CODE_ASSIGNMENT}, il se trouve dans le même format que les README des différents travaux que vous avez eu. 
Si vous souhaitez une recorrection ou un éclaircissement de votre note, je vous invite à m'écrire sur Discord, de répondre à ce courriel ou de venir me voir durant les heures de cours !

Bonne journée ! 
Faneva Rakotoarivony
"""

def build_mail(sender: str, receiver: list[str], subject: str, message: str, attachments: list[MailAttachment] = [])->MIMEMultipart: 
    email = MIMEMultipart()

    email["Subject"] = subject
    email["From"] = sender
    email["To"] = ", ".join(receiver)
    email.attach(MIMEText(message))

    for attachment in attachments: 
        try: 
            os.stat(attachment.path)
            email.attach(attachment.to_MIME())
        except Exception: 
            print(f"Attachment {attachment.path} not found")
            continue
    return email

def send_mails(messages: list[MIMEMultipart], smtp_addr: str = "smtp.polymtl.ca", port: int = 587):
    server = smtplib.SMTP(smtp_addr, port)
    server.starttls()

    server.login(CORRECTOR_MAIL_USERNAME, CORRECTOR_MAIL_PASSWORD)

    for message in messages: 
        server.send_message(message)
    server.quit()
