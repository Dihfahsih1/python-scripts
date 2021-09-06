from os import error
import smtplib
import  csv 
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import  MIMEBase
from email import encoders

import schedule
import time

# training@rcsconsult.net,Racheal,Agitta,+971-585-554-431
# isaac@rcsconsult.net,Isaac,Malagala,+971-525-557-934
# office@rcsconsult.net,Ivan,Igaga,+971-525-557-934
# operations@begos.biz, Ibra, Kaima.+25678749058

def mass_mailing_script():
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

schedule.every().monday.at("08:43").do(mass_mailing_script)

while True:
    schedule.run_pending()
    time.sleep(1)