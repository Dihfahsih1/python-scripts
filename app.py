from os import error
import smtplib
import  csv 
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=11, minute=50)
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
                message = "Hello "
                subject ="Testing the webinnar mass mailing" 
                html_body =open("how_to_build_high_performance_teams.html")
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

 