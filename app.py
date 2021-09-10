from os import error
import smtplib
import  csv 
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler
import time

sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=13, minute=17)
def mass_mailing_script():
    email_user = "office@rcsconsult.net"
    password = "**1234office"
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    with open('cleaned_emails.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        try:
            count = 0
            for line in reader:
                if(len(line) < 1):
                    continue
                email_send = line[0]
                subject ="Training Webinar" 
                html_body =open("how_to_build_high_performance_teams.html")
                msg = MIMEText(html_body.read(), "html")
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject
                
                text = msg.as_string()
                server.login(email_user, password)
                server.sendmail(email_user, email_send, text)
                count +=1
                print(str(count) + ". Sent Email to: " + email_send)
                
                if(count%20 == 0):
                    print("Server Cooldown for 05 seconds")
                    time.sleep(20)
                    server.ehlo()
                    server.login(email_user, password)
                    
        except:
            print("error") 
sched.start()

