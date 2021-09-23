import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='ict@rcsconsult.net',
    
    to_emails=['dihfahsih@gmail.com','dihfahsihm@gmail.com','mugdih@outlook.com'],
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    SENDGRID_API_KEY = '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'

    sg = SendGridAPIClient(SENDGRID_API_KEY )
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)