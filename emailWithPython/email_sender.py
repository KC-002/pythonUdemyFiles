import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Praveen Kumar KC'
email['to'] = 'xe.000054@gmail.com'
email['subject'] = 'Performance'

email.set_content('Hey! You are doing a good job improving skills. Keep it up!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyuser.batman@gmail.com', 'justiceonfist')
    smtp.send_message(email)
