from os import error
import smtplib
import  csv 
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import  MIMEBase
from email import encoders

import schedule
import time
from apscheduler.schedulers.blocking import BlockingScheduler

# training@rcsconsult.net,Racheal,Agitta,+971-585-554-431
# isaac@rcsconsult.net,Isaac,Malagala,+971-525-557-934
# office@rcsconsult.net,Ivan,Igaga,+971-525-557-934
# operations@begos.biz, Ibra, Kaima.+25678749058

sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=16, minute=30)
def mass_mailing_script():
    email_user = "ict@rcsconsult.net"
    password = "pythonista"
    
    file = "text.txt"
    with open('receipients.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        try:
            for line in reader:
                if(len(line) < 1):
                    continue
                email_send = line[0]
                message = "Hello " +line[1]+"," 
                subject ="RCS Company data or files backup" 
                html_body =open("text.html")
                msg = MIMEText(html_body.read(), "html")
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject
                msg['Message'] = message
                
                text = msg.as_string()
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(email_user, password)
                server.sendmail(email_user, email_send, text)
                
                server.quit()
                print("emails were sent")
        except:
            print(error.message)

sched.start()

#procfile