import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Praveen Kumar KC'
email['to']= 'kc.praveenkumar002@gmail.com'
email['subject'] = 'You have Won RS10,0....'

email.set_content(html.substitute({'name' : 'Praveen'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyuser.batman@gmail.com', 'justiceonfist')
    smtp.send_message(email)