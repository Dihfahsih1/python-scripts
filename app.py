from os import error
import smtplib
import  csv 
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import  MIMEBase
from email import encoders


email_user = "ict@rcsconsult.net"
password = "pythonista"
subject =" Testing" 
file = "text.txt"
with open('receipients.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    try:
        for line in reader:
            if(len(line) < 1):
                continue
            text = "Hello " +line[1]+"," + " we are contacting you"
            email_send = line[0]
            html_body =open("text.html")
            msg = MIMEText(html_body.read(), "html")
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject
            
            text = msg.as_string()
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(email_user, password)
            server.sendmail(email_user, email_send, text)
            
            server.quit()
    except:
        print(error.message)