from os import error
import smtplib
import  csv 
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import  MIMEBase
from email import encoders
import pandas as pd

import schedule
import time
from apscheduler.schedulers.blocking import BlockingScheduler



sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=00, minute=30)
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
                subject ="Follow up email on back up" 
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