from os import error
import smtplib
import  csv 
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler

def mass_mailing_script():
    email_user = "office@rcsconsult.net"
    password = "office**1234"
    
    print(email_user)
    with open('cleaned_emails.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        try:
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
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(email_user, password)
                server.sendmail(email_user, email_send, text)
                
                server.quit()
        except:
            print(error.message)

mass_mailing_script()