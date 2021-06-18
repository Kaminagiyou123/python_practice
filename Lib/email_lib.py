
import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['subject']='Test Email'
email['From']='ran.you8311@gmail.com'
email['To']='someone@gmail.com'
email.set_content("blahblahblah")
conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('ran.you8311@gmail.com','XXXXXXXX')
conn.send_message(email)
conn.quit()